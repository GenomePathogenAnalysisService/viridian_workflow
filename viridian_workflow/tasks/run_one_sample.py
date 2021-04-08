from viridian_workflow import one_sample_pipeline


def run(options):
    one_sample_pipeline.run_one_sample(
        options.outdir,
        options.ref_fasta,
        options.amplicon_bed,
        options.fastq1,
        options.fastq2,
    )