"""
流失用户分析完整代码
包含：相关性分析、卡方检验、XGBoost 模型、目标用户识别
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr, spearmanr
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class ChurnAnalysis:
    def __init__(self, data_path=None):
        """初始化流失用户分析类"""
        self.df = None
        self.model = None
        self.feature_importance = None
        self.target_users = None

        if data_path:
            self.load_data(data_path)

    def load_data(self, data_path):
        """加载数据"""
        self.df = pd.read_csv(data_path)
        print(f"数据加载成功，形状: {self.df.shape}")
        print(f"数据列: {self.df.columns.tolist()}")
        return self.df

    def create_sample_data(self):
        """创建示例数据（如果没有真实数据）"""
        np.random.seed(42)
        n_samples = 1000

        self.df = pd.DataFrame({
            'user_id': range(1, n_samples + 1),
            'age': np.random.randint(18, 70, n_samples),
            'tenure_months': np.random.randint(1, 60, n_samples),
            'monthly_charges': np.random.uniform(20, 150, n_samples),
            'total_charges': np.random.uniform(100, 5000, n_samples),
            'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples),
            'internet_service': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples),
            'online_security': np.random.choice(['Yes', 'No'], n_samples),
            'tech_support': np.random.choice(['Yes', 'No'], n_samples),
            'payment_method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_samples),
            'churn': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])  # 30% 流失率
        })

        print(f"示例数据创建成功，形状: {self.df.shape}")
        return self.df

    def correlation_analysis(self):
        """相关性分析"""
        print("\n" + "="*50)
        print("相关性分析")
        print("="*50)

        # 数值型特征与流失的相关性
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        if 'churn' in numeric_cols:
            numeric_cols.remove('churn')
        if 'user_id' in numeric_cols:
            numeric_cols.remove('user_id')

        correlations = {}
        for col in numeric_cols:
            # 皮尔逊相关系数
            corr, p_value = pearsonr(self.df[col], self.df['churn'])
            correlations[col] = {'pearson': corr, 'p_value': p_value}
            print(f"{col}: 相关系数={corr:.4f}, p值={p_value:.4f}")

        return correlations

    def chi_square_test(self):
        """卡方检验（分类变量与流失的关系）"""
        print("\n" + "="*50)
        print("卡方检验（分类变量）")
        print("="*50)

        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        chi_square_results = {}

        for col in categorical_cols:
            # 创建交叉表
            contingency_table = pd.crosstab(self.df[col], self.df['churn'])
            chi2, p_value, dof, expected = chi2_contingency(contingency_table)

            chi_square_results[col] = {
                'chi2': chi2,
                'p_value': p_value,
                'dof': dof
            }

            print(f"\n{col}:")
            print(f"  卡方值: {chi2:.4f}")
            print(f"  p值: {p_value:.4f}")
            print(f"  显著性: {'显著' if p_value < 0.05 else '不显著'}")

        return chi_square_results

    def data_preprocessing(self):
        """数据预处理"""
        print("\n" + "="*50)
        print("数据预处理")
        print("="*50)

        df_processed = self.df.copy()

        # 处理缺失值
        print(f"缺失值:\n{df_processed.isnull().sum()}")
        df_processed = df_processed.dropna()

        # 编码分类变量
        le_dict = {}
        categorical_cols = df_processed.select_dtypes(include=['object']).columns.tolist()

        for col in categorical_cols:
            le = LabelEncoder()
            df_processed[col] = le.fit_transform(df_processed[col])
            le_dict[col] = le
            print(f"{col} 编码完成")

        return df_processed, le_dict

    def train_xgboost_model(self, test_size=0.2):
        """训练 XGBoost 模型"""
        print("\n" + "="*50)
        print("XGBoost 模型训练")
        print("="*50)

        # 数据预处理
        df_processed, le_dict = self.data_preprocessing()

        # 分离特征和目标
        X = df_processed.drop(['churn', 'user_id'], axis=1)
        y = df_processed['churn']

        # 划分训练集和测试集
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y
        )

        print(f"训练集大小: {X_train.shape}")
        print(f"测试集大小: {X_test.shape}")

        # 训练 XGBoost 模型
        self.model = xgb.XGBClassifier(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            eval_metric='logloss'
        )

        self.model.fit(X_train, y_train, verbose=False)

        # 模型评估
        y_pred = self.model.predict(X_test)
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]

        print("\n模型性能:")
        print(classification_report(y_test, y_pred, target_names=['保留', '流失']))

        # ROC-AUC
        auc_score = roc_auc_score(y_test, y_pred_proba)
        print(f"ROC-AUC 分数: {auc_score:.4f}")

        # 特征重要性
        self.feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)

        print("\n特征重要性 Top 10:")
        print(self.feature_importance.head(10))

        return self.model, X_test, y_test, y_pred_proba

    def identify_target_users(self, churn_threshold=0.5):
        """识别目标用户（高流失风险用户）"""
        print("\n" + "="*50)
        print("目标用户识别")
        print("="*50)

        # 数据预处理
        df_processed, le_dict = self.data_preprocessing()

        # 预测所有用户的流失概率
        X_all = df_processed.drop(['churn', 'user_id'], axis=1)
        churn_proba = self.model.predict_proba(X_all)[:, 1]

        # 添加预测结果到原始数据
        df_processed['churn_probability'] = churn_proba
        df_processed['churn_prediction'] = (churn_proba >= churn_threshold).astype(int)

        # 识别高风险用户
        target_users = df_processed[df_processed['churn_probability'] >= churn_threshold].copy()
        target_users = target_users.sort_values('churn_probability', ascending=False)

        print(f"\n高风险用户数量: {len(target_users)}")
        print(f"高风险用户占比: {len(target_users)/len(df_processed)*100:.2f}%")

        # 合并原始用户ID
        target_users['user_id'] = self.df.iloc[target_users.index]['user_id'].values

        self.target_users = target_users

        return target_users

    def export_target_users(self, output_path='target_users.csv'):
        """导出目标用户"""
        if self.target_users is not None:
            # 选择关键列
            export_cols = ['user_id', 'churn_probability', 'churn_prediction']
            # 添加原始特征中的关键列
            for col in self.df.columns:
                if col not in ['user_id', 'churn']:
                    if col in self.target_users.columns:
                        export_cols.append(col)

            export_df = self.target_users[export_cols[:10]].copy()  # 限制列数
            export_df.to_csv(output_path, index=False, encoding='utf-8-sig')
            print(f"\n目标用户已导出到: {output_path}")
            print(f"导出用户数: {len(export_df)}")
            return export_df
        else:
            print("请先识别目标用户")
            return None

    def visualize_results(self):
        """可视化分析结果"""
        print("\n" + "="*50)
        print("生成可视化图表")
        print("="*50)

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # 1. 特征重要性
        if self.feature_importance is not None:
            top_features = self.feature_importance.head(10)
            axes[0, 0].barh(top_features['feature'], top_features['importance'])
            axes[0, 0].set_title('特征重要性 Top 10')
            axes[0, 0].set_xlabel('重要性')

        # 2. 流失概率分布
        if self.target_users is not None:
            axes[0, 1].hist(self.target_users['churn_probability'], bins=30, edgecolor='black')
            axes[0, 1].set_title('高风险用户流失概率分布')
            axes[0, 1].set_xlabel('流失概率')
            axes[0, 1].set_ylabel('用户数')

        # 3. 流失率对比
        churn_rate = self.df['churn'].value_counts()
        axes[1, 0].bar(['保留', '流失'], churn_rate.values)
        axes[1, 0].set_title('用户流失率')
        axes[1, 0].set_ylabel('用户数')

        # 4. 流失用户特征对比
        if 'tenure_months' in self.df.columns:
            axes[1, 1].boxplot([
                self.df[self.df['churn'] == 0]['tenure_months'],
                self.df[self.df['churn'] == 1]['tenure_months']
            ], labels=['保留', '流失'])
            axes[1, 1].set_title('用户任期对比')
            axes[1, 1].set_ylabel('任期（月）')

        plt.tight_layout()
        plt.savefig('churn_analysis_results.png', dpi=300, bbox_inches='tight')
        print("图表已保存为: churn_analysis_results.png")
        plt.show()


def main():
    """主函数"""
    # 初始化分析器
    analyzer = ChurnAnalysis()

    # 创建示例数据（或使用 analyzer.load_data('your_data.csv')）
    analyzer.create_sample_data()

    # 1. 相关性分析
    correlations = analyzer.correlation_analysis()

    # 2. 卡方检验
    chi_square_results = analyzer.chi_square_test()

    # 3. 训练 XGBoost 模型
    model, X_test, y_test, y_pred_proba = analyzer.train_xgboost_model()

    # 4. 识别目标用户
    target_users = analyzer.identify_target_users(churn_threshold=0.5)

    # 5. 导出目标用户
    export_df = analyzer.export_target_users('target_users.csv')

    # 6. 可视化结果
    analyzer.visualize_results()

    # 7. 输出目标用户详情
    print("\n" + "="*50)
    print("目标用户详情（前 10 个）")
    print("="*50)
    print(target_users[['user_id', 'churn_probability']].head(10))


if __name__ == '__main__':
    main()
