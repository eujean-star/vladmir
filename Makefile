setup:
	conda env create --file environment.yml

download_fastq_data:
	mkdir -p data/raw && \
	cd data/raw && \
	wget -O vladmir-raw-data.tar.gz https://omixlab-vladimir-data.s3.amazonaws.com/vladmir-raw-data.tar.gz && \
	tar -xvf vladmir-raw-data.tar.gz && \
	mv raw fastq && \
	rm vladmir-raw-data.tar.gz

download_kmer_data:
	mkdir -p data/raw && \
	cd data/raw && \
	wget -O vladmir-kmers-data.tar.gz https://omixlab-vladimir-data.s3.amazonaws.com/vladmir-kmers-data.tar.gz && \
	tar -xvf vladmir-kmers-data.tar.gz && \
	rm vladmir-kmers-data.tar.gz