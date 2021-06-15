setup:
	conda env create --file environment.yml || conda env update --file environment.yml

tools:
	conda install -c bioconda sra-tools | conda install -c bioconda jellyfish