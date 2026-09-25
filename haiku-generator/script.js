// DOM Elements
const textInput = document.getElementById('textInput');
const generateBtn = document.getElementById('generateBtn');
const clearBtn = document.getElementById('clearBtn');
const loadingState = document.getElementById('loadingState');
const resultsSection = document.getElementById('resultsSection');
const haikuContainer = document.getElementById('haikuContainer');
const copyBtn = document.getElementById('copyBtn');

// State
let currentHaikus = [];

// Event Listeners
generateBtn.addEventListener('click', generateHaiku);
clearBtn.addEventListener('click', clearInput);
copyBtn.addEventListener('click', copyToClipboard);

// Simulate AI haiku generation (replace with actual AI API call)
async function generateHaiku() {
    const inputText = textInput.value.trim();

    if (!inputText) {
        showNotification('Please enter some text first!', 'error');
        return;
    }

    // Show loading state
    resultsSection.classList.add('hidden');
    loadingState.classList.remove('hidden');
    generateBtn.disabled = true;

    try {
        // Simulate API call delay
        await new Promise(resolve => setTimeout(resolve, 1500));

        // Generate haikus using AI logic (simplified version)
        const haikus = createHaikusFromText(inputText);
        currentHaikus = haikus;

        displayHaikus(haikus);

        // Hide loading, show results
        loadingState.classList.add('hidden');
        resultsSection.classList.remove('hidden');

        // Smooth scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    } catch (error) {
        showNotification('Oops! Something went wrong. Please try again.', 'error');
        loadingState.classList.add('hidden');
    } finally {
        generateBtn.disabled = false;
    }
}

// Create haikus from text (AI simulation)
function createHaikusFromText(text) {
    // This is a simplified version. In production, you'd call an AI API
    const words = text.split(/\s+/).filter(w => w.length > 0);
    const numHaikus = Math.min(3, Math.max(1, Math.floor(words.length / 15)));

    const haikus = [];
    const templates = [
        {
            structure: [5, 7, 5],
            lines: [
                ['Ancient', 'Digital', 'Whispers', 'Silent', 'Golden'],
                ['Dancing through the morning light', 'Echoing in distant dreams', 'Flowing like a gentle stream'],
                ['Peace finds', 'Time flows', 'Dreams bloom', 'Hope grows', 'Love stays']
            ]
        },
        {
            structure: [5, 7, 5],
            lines: [
                ['Moonlight', 'Starlit', 'Twilight', 'Sunset', 'Daybreak'],
                ['Painting shadows on the wall', 'Whispers carried by the wind', 'Dancing leaves in autumn chill'],
                ['Life begins', 'Hearts unite', 'Souls connect', 'Worlds align', 'Time bends']
            ]
        },
        {
            structure: [5, 7, 5],
            lines: [
                ['Beneath', 'Beyond', 'Within', 'Above', 'Around'],
                ['The endless sky of possibility', 'Where dreams and reality merge', 'Through memories we once shared'],
                ['We discover', 'We become', 'We transcend', 'We believe', 'We shine bright']
            ]
        }
    ];

    for (let i = 0; i < numHaikus; i++) {
        const template = templates[i % templates.length];
        const haiku = {
            lines: [
                getRandomElement(template.lines[0]) + ' whispers',
                getRandomElement(template.lines[1]),
                getRandomElement(template.lines[2])
            ],
            syllables: template.structure
        };
        haikus.push(haiku);
    }

    return haikus;
}

function getRandomElement(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

// Display haikus
function displayHaikus(haikus) {
    haikuContainer.innerHTML = '';

    haikus.forEach((haiku, index) => {
        const card = document.createElement('div');
        card.className = 'haiku-card';
        card.style.animationDelay = `${index * 0.1}s`;

        const lines = document.createElement('div');
        lines.className = 'haiku-lines';

        haiku.lines.forEach(line => {
            const lineElement = document.createElement('span');
            lineElement.className = 'haiku-line';
            lineElement.textContent = line;
            lines.appendChild(lineElement);
        });

        const meta = document.createElement('div');
        meta.className = 'haiku-meta';
        meta.innerHTML = `
            <span class="syllable-count">${haiku.syllables.join('-')} syllables</span>
            <span>Haiku ${index + 1} of ${haikus.length}</span>
        `;

        card.appendChild(lines);
        card.appendChild(meta);
        haikuContainer.appendChild(card);
    });
}

// Clear input
function clearInput() {
    textInput.value = '';
    resultsSection.classList.add('hidden');
    currentHaikus = [];
    textInput.focus();
}

// Copy to clipboard
async function copyToClipboard() {
    const text = currentHaikus.map(h => h.lines.join('\n')).join('\n\n---\n\n');

    try {
        await navigator.clipboard.writeText(text);
        showNotification('Copied to clipboard!', 'success');
    } catch (error) {
        showNotification('Failed to copy', 'error');
    }
}

// Notification system
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        background: ${type === 'error' ? '#EF4444' : '#4FD1C5'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        animation: slideInRight 0.3s ease-out;
        z-index: 1000;
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add notification animations to CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
