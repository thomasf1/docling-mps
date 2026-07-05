<p align="center">
  <a href="https://github.com/docling-project/docling">
    <img loading="lazy" alt="Docling" src="https://github.com/docling-project/docling/raw/main/docs/assets/docling_processing.png" width="100%"/>
  </a>
</p>

# Docling

<p align="center">
  <a href="https://trendshift.io/repositories/17240" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17240" alt="DS4SD%2Fdocling | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

[![arXiv](https://img.shields.io/badge/arXiv-2408.09869-b31b1b.svg)](https://arxiv.org/abs/2408.09869)
[![Docs](https://img.shields.io/badge/docs-live-brightgreen)](https://docling-project.github.io/docling/)
[![PyPI version](https://img.shields.io/pypi/v/docling)](https://pypi.org/project/docling/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/docling)](https://pypi.org/project/docling/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
[![prek](https://img.shields.io/badge/prek-enabled-brightgreen)](https://pypi.org/project/prek/)
[![License MIT](https://img.shields.io/github/license/docling-project/docling)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](https://static.pepy.tech/badge/docling/month)](https://pepy.tech/projects/docling)
[![Docling Actor](https://apify.com/actor-badge?actor=vancura/docling&fpr=docling)](https://apify.com/vancura/docling)
[![Chat with Dosu](https://dosu.dev/dosu-chat-badge.svg)](https://app.dosu.dev/097760a8-135e-4789-8234-90c8837d7f1c/ask?utm_source=github)
[![Discord](https://img.shields.io/discord/1399788921306746971?color=6A7EC2&logo=discord&logoColor=ffffff)](https://docling.ai/discord)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10101/badge)](https://www.bestpractices.dev/projects/10101)
[![LF AI & Data](https://img.shields.io/badge/LF%20AI%20%26%20Data-003778?logo=linuxfoundation&logoColor=fff&color=0094ff&labelColor=003778)](https://lfaidata.foundation/projects/)

## What is Docling ?

Docling simplifies document processing by parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the generative AI ecosystem.

## Features

- 🗂️ Parsing of [multiple document formats][supported_formats] including PDF, DOCX, PPTX, XLSX, HTML, EPUB, WAV, MP3, WebVTT, email formats (EML, MSG), images (PNG, TIFF, JPEG, ...), LaTeX, DocLang, plain text, and more
- 📑 Advanced PDF understanding incl. page layout, reading order, table structure, code, formulas, image classification, and more
- 🧬 A unified, expressive [DoclingDocument][docling_document] representation format
- ↪️ Various [export formats][supported_formats] and options, including Markdown, HTML, WebVTT, DocLang, [DocTags](https://arxiv.org/abs/2503.11576) and lossless JSON
- 📜 Support for several application-specific XML schemas including [DocLang](https://doclang.ai), [USPTO](https://www.uspto.gov/patents) patents, [JATS](https://jats.nlm.nih.gov/) articles, and [XBRL](https://www.xbrl.org/) financial reports.
- 🔒 Local execution capabilities for sensitive data and air-gapped environments
- 🤖 Plug-and-play [integrations][integrations] incl. LangChain, LlamaIndex, Crew AI & Haystack for agentic AI
- 🔍 Extensive OCR support for scanned PDFs and images
- 👓 Support for several Visual Language Models, such as ([GraniteDocling](https://huggingface.co/ibm-granite/granite-docling-258M))
- 🎙️ Audio support with Automatic Speech Recognition (ASR) models
- 🔌 Connect to any agent using the [MCP server](https://docling-project.github.io/docling/usage/mcp/)
- 🌐 Run Docling as a service with the [API server](https://docling-project.github.io/docling/usage/api_server/) (docling-serve)
- 💻 Simple and convenient CLI

### What's new

- 📄 Parsing of ODF (OpenDocument Format) files for text documents (`.odt`), spreadsheets (`.ods`), and presentations (`.odp`)
- 💼 Parsing of XBRL (eXtensible Business Reporting Language) documents for financial reports
- 📧 Parsing of email files (`.eml`, `.msg`)
- 📚 Parsing of EPUB (Electronic Publication) files for e-books
- 📝 Parsing of plain-text files (`.txt`, `.text`) and Markdown supersets (`.qmd`, `.Rmd`)
- 📊 Chart understanding (Barchart, Piechart, LinePlot): convert them into tables or code and add detailed descriptions

### Coming soon

- 📝 Metadata extraction, including title, authors, references & language
- 📝 Complex chemistry understanding (Molecular structures)

## Quickstart

### 1. Install

```bash
pip install docling
```

> **Note:** Python 3.9 support was dropped in docling version 2.70.0. Please use Python 3.10 or higher.

Works on macOS, Linux and Windows environments for both x86_64 and arm64 architectures.

More [detailed installation instructions](https://docling-project.github.io/docling/getting_started/installation/) are available in the docs.

## 2. Convert a document (CLI)

```bash
docling https://arxiv.org/pdf/2206.01062
```

This generates a .md file in the current directory containing structured document content.

You can also use 🥚[GraniteDocling](https://huggingface.co/ibm-granite/granite-docling-258M) and other VLMs via Docling CLI:

```bash
docling --pipeline vlm --vlm-model granite_docling https://arxiv.org/pdf/2206.01062
```

## 3. Python usage (recommended)

```python
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # a document via a local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
```

More advanced [usage](https://docling-project.github.io/docling/usage/) and [configuration](https://docling-project.github.io/docling/getting_started/installation/) options.

## Documentation

Check out Docling's [documentation](https://docling-project.github.io/docling/) for details on
installation, usage, concepts, recipes, extensions, and more.

## Examples

Go hands-on with our [examples](https://docling-project.github.io/docling/examples/),
demonstrating how to address different application use cases with Docling.

## Integrations

To further accelerate your AI application development, check out Docling's native
[integrations](https://docling-project.github.io/docling/integrations/) with popular frameworks
and tools.

## Get help and support

Please feel free to connect with us using the [discussion section](https://github.com/docling-project/docling/discussions).

## Technical report

For more details on Docling's inner workings, check out the [Docling Technical Report](https://arxiv.org/abs/2408.09869).

## Contributing

Please read [Contributing to Docling](https://github.com/docling-project/docling/blob/main/CONTRIBUTING.md) for details.

## References

If you use Docling in your projects, please consider citing the following:

```bib
@techreport{Docling,
  author = {Deep Search Team},
  month = {8},
  title = {Docling Technical Report},
  url = {https://arxiv.org/abs/2408.09869},
  eprint = {2408.09869},
  doi = {10.48550/arXiv.2408.09869},
  version = {1.0.0},
  year = {2024}
}
```

## Apple Silicon Optimizations & Benchmarks

This local version (`2.107.0+mps`) has been optimized to fully leverage Apple Silicon hardware (M-series chips) for document processing.

### Optimizations
- **MPS (Metal Performance Shaders) Enablement**: Removed CPU fallbacks for TableFormer V1 & V2 models, enabling standard PyTorch operations to execute natively on the GPU instead of CPU.
- **VLM Presets for Apple Silicon**: Added `GRANITEDOCLING` and `SMOLDOCLING` constants that dynamically select highly-optimized local `mlx-vlm` models on Apple Silicon.

### Benchmark Results (TableFormer V1 Accurate Mode)
Timings measured for processing financial reports in `/Volumes/18T/Annual/scratch/comparison` (156-page PDF documents) sequentially:

| PDF Document | Configuration | Processing Time (s) | Output Chars | Speedup vs CPU | Speedup vs MPS |
|---|---|---|---|---|---|
| **NASDAQ_LPCN_2023.pdf** | PyTorch CPU | 102.56s | 604,940 | 1.00x | 0.49x |
| | PyTorch MPS | 50.46s | 604,940 | **2.03x** | **1.00x** |
| **NYSE_ITT_2023.pdf** | PyTorch CPU | 121.35s | 453,126 | 1.00x | 0.49x |
| | PyTorch MPS | 59.24s | 453,126 | **2.05x** | **1.00x** |
| **OTC_SOMC_2023.pdf** | PyTorch CPU | 115.56s | 340,292 | 1.00x | 0.53x |
| | PyTorch MPS | 61.19s | 340,292 | **1.89x** | **1.00x** |

### Concurrent Workload Benchmark (Parallel Processing)
Concurrently processing all 3 documents using parallel Python subprocesses:
* **PyTorch CPU Parallel**: **226.53 seconds** (1.00x)
* **PyTorch MPS Parallel**: **110.61 seconds** (**2.05x speedup** vs CPU)

### CoreML & MLX Hardware Contention (Why they didn't pan out)

We also researched, converted, and benchmarked TableFormer V1's encoder to CoreML (linear quantized to INT8 for the Neural Engine) and MLX (GPU), and the Layout Model (RT-DETR) to ONNX running on Apple's `CoreMLExecutionProvider`. While successfully running with 100% numerical correctness, these backends did not outperform PyTorch MPS due to native platform architectural constraints:

1. **Graph Partitioning & Context Switching Overhead (Layout Model)**:
   - Because RT-DETR contains custom post-processing nodes unsupported by CoreML, ONNX Runtime split the model into **28 separate CoreML partitions**.
   - Transitioning between CoreML hardware execution and CPU fallback nodes required copying intermediate tensor data between ANE memory and system RAM 28 times per page. This context switching and memory copy overhead offset the ANE's raw processing speedup, making Layout CoreML (64.29s) slower than running natively on GPU via PyTorch MPS (50.46s).

2. **Apple Neural Engine (ANE) Multi-Process Contention**:
   - When attempting to run parallel document conversions concurrently under multiprocessing, Apple's E5/ANE runtime suffered from **compilation cache and file-lock collisions** on the compiled macho assets inside `/var/folders/`, throwing on-device model load failures (`ANE model load has failed...`).
   - This forced CoreML to fallback to silent CPU execution. The resulting core thread contention degraded parallel throughput significantly (**137.53s** wall time) compared to the hardware time-sliced GPU command queue multiplexing of **PyTorch MPS** (**110.61s**).

Thus, native **PyTorch MPS (GPU)** remains the most robust, performant, and scale-friendly backend for Docling on Apple Silicon.

## License

The Docling codebase is under MIT license.
For individual model usage, please refer to the model licenses found in the original packages.

## LF AI & Data

Docling is hosted as a project in the [LF AI & Data Foundation](https://lfaidata.foundation/projects/).

### IBM ❤️ Open Source AI

The project was started by the AI for knowledge team at IBM Research Zurich.

[supported_formats]: https://docling-project.github.io/docling/usage/supported_formats/
[docling_document]: https://docling-project.github.io/docling/concepts/docling_document/
[integrations]: https://docling-project.github.io/docling/integrations/
[extraction]: https://docling-project.github.io/docling/_generated/examples/extraction/
