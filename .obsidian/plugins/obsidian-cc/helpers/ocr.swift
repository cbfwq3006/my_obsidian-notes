#!/usr/bin/env swift
//
// obsidian-cc — macOS OCR helper (Apple Vision framework)
//
// On-device OCR: no dependencies, no network, no API key. Called by the
// plugin's agent-bridge "vision gate" when the configured model does NOT accept
// images — it turns a raw/ screenshot into text so the agent can still digest
// it. This is the privacy-friendly, zero-cost counterpart to model vision.
//
//   swift ocr.swift <image-path>        -> recognized text on stdout
//
// Prints nothing (exit 0) when no text is recognized; the plugin then falls
// back to its "image skipped" notice. Exits nonzero on load/OCR errors.
//
// Requires macOS 13 (Ventura) or newer for Chinese (zh-Hans / zh-Hant).
// Mixed CJK + Latin is handled by listing several recognitionLanguages.

import AppKit
import Vision

guard CommandLine.arguments.count >= 2 else {
    FileHandle.standardError.write("usage: ocr.swift <image-path>\n".data(using: .utf8)!)
    exit(64)
}
let imagePath = CommandLine.arguments[1]

guard
    let nsImage = NSImage(contentsOfFile: imagePath),
    let tiff = nsImage.tiffRepresentation,
    let rep = NSBitmapImageRep(data: tiff),
    let cgImage = rep.cgImage
else {
    FileHandle.standardError.write("error: cannot load image: \(imagePath)\n".data(using: .utf8)!)
    exit(1)
}

let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate                  // accurate is required for CJK
request.recognitionLanguages = ["zh-Hans", "zh-Hant", "en-US"]
request.usesLanguageCorrection = true

let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
do {
    try handler.perform([request])
} catch {
    FileHandle.standardError.write("error: OCR failed: \(error)\n".data(using: .utf8)!)
    exit(1)
}

let lines = (request.results ?? [])
    .compactMap { $0.topCandidates(1).first?.string }

if lines.isEmpty { exit(0) }                          // no text -> empty stdout
print(lines.joined(separator: "\n"))
