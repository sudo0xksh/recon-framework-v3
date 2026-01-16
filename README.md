# 🔍 Recon Framework v3

Recon Framework v3 is a Python-based CLI tool that automates multiple
reconnaissance and vulnerability scanning steps into a single workflow.

It is an evolution of earlier versions, adding more modules and better
coverage of the typical reconnaissance process.

---

## Overview

Real-world reconnaissance is not a single tool.
It is a sequence of steps that work together.

Recon Framework v3 automates this sequence by combining:
- Web crawling
- XSS scanning
- Optional SQL injection testing
- Nmap scanning

Instead of running each tool manually, this framework orchestrates them
from one entry point.

---

## Features

- Centralized recon orchestration
- Runs an internal web crawler
- Executes XSS scanner automatically
- Optional SQL injection testing
- Integrates Nmap scanning
- Generates text and JSON summary reports
- Designed for modular growth

---

## How It Works

The framework accepts a target URL and an optional parameter.

Execution flow:
1. Crawls the target website and saves discovered pages
2. Runs the XSS scanner against the target
3. Runs the SQLi scanner if a parameter is provided
4. Executes an Nmap scan
5. Generates consolidated report files

Each module is executed using subprocess calls, keeping the framework
simple and extensible.

---

## Usage

Run the framework like this  
python recon_frameworkv3.py -u <url>

To include SQL injection testing  
python recon_frameworkv3.py -u <url> -p <parameter>

The framework automatically decides which modules to run based on input.

---

## Output

The framework generates:
- `crawler_output.txt` for crawled pages
- `xss_report.txt` for XSS findings
- SQLi scan output (if executed)
- `nmap_report.json` for Nmap results
- `recon_report.txt` as a human-readable summary
- `recon_report.json` as a structured report

---

## Requirements

- Python 3.x
- requests library
- All dependent scripts present in the same directory:
  - crawler.py
  - xss_scanner.py
  - sqli_scanner.py
  - nmap_scan.py

Install dependencies if needed  
pip install requests

---

## Notes

- SQLi scanning is skipped if no parameter is provided
- Output depends on individual scanner behavior
- Intended strictly for learning and authorized testing

---

## Final Thoughts

Recon Framework v3 is about understanding flow, not exploitation.

Once you can chain tools together cleanly,
you are thinking like a tool builder, not just a user.
