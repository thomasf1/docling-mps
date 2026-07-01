import argparse
import json
import os
import time
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    TableFormerMode,
    TableStructureOptions,
    TableStructureV2Options,
)
from docling.document_converter import DocumentConverter, PdfFormatOption

PDF_FILES = [
    "NASDAQ_LPCN_2023.pdf",
    "NYSE_ITT_2023.pdf",
    "OTC_SOMC_2023.pdf",
]

def run_benchmark(pdf_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    results = {}

    for pdf_name in PDF_FILES:
        pdf_path = pdf_dir / pdf_name
        if not pdf_path.exists():
            print(f"Skipping {pdf_name}: file not found at {pdf_path}")
            continue

        results[pdf_name] = {}
        print(f"\nProcessing {pdf_name}...")

        # Benchmark 1: TableFormer V1 Accurate
        print("  Running TableFormer V1 (Accurate Mode)...")
        options_v1 = PdfPipelineOptions()
        options_v1.table_structure_options = TableStructureOptions(
            mode=TableFormerMode.ACCURATE
        )
        converter_v1 = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=options_v1)
            }
        )

        start_time = time.perf_counter()
        conv_res_v1 = converter_v1.convert(pdf_path)
        elapsed_v1 = time.perf_counter() - start_time
        print(f"    Done in {elapsed_v1:.2f} seconds.")

        # Save output markdown
        md_content_v1 = conv_res_v1.document.export_to_markdown()
        md_file_v1 = output_dir / f"{pdf_path.stem}_v1_accurate.md"
        md_file_v1.write_text(md_content_v1, encoding="utf-8")
        results[pdf_name]["v1_accurate"] = {
            "time_seconds": elapsed_v1,
            "char_count": len(md_content_v1),
            "file_size_bytes": md_file_v1.stat().st_size,
        }

        # Benchmark 2: TableFormer V2
        print("  Running TableFormer V2...")
        options_v2 = PdfPipelineOptions()
        options_v2.table_structure_options = TableStructureV2Options()
        converter_v2 = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=options_v2)
            }
        )

        start_time = time.perf_counter()
        conv_res_v2 = converter_v2.convert(pdf_path)
        elapsed_v2 = time.perf_counter() - start_time
        print(f"    Done in {elapsed_v2:.2f} seconds.")

        # Save output markdown
        md_content_v2 = conv_res_v2.document.export_to_markdown()
        md_file_v2 = output_dir / f"{pdf_path.stem}_v2.md"
        md_file_v2.write_text(md_content_v2, encoding="utf-8")
        results[pdf_name]["v2"] = {
            "time_seconds": elapsed_v2,
            "char_count": len(md_content_v2),
            "file_size_bytes": md_file_v2.stat().st_size,
        }

    # Write summary report
    summary_path = output_dir / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\nBenchmark completed!")
    print(f"Summary JSON saved to {summary_path}")

    # Display results
    print("\n| PDF File | Model Configuration | Processing Time (s) | Output Chars |")
    print("|---|---|---|---|")
    for pdf_name, configs in results.items():
        for config_name, stats in configs.items():
            print(f"| {pdf_name} | {config_name} | {stats['time_seconds']:.2f}s | {stats['char_count']:,} |")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", type=str, default="/Volumes/18T/Annual/scratch/comparison")
    parser.add_argument("--output-dir", type=str, required=True)
    args = parser.parse_args()

    run_benchmark(Path(args.pdf_dir), Path(args.output_dir))
