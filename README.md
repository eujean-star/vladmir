# VladmiR
- Vladmir is a tool to predict alzheimer deasease from a  set of relative count kmers SRA data from NCBI. 



In progress...  



## Project structure

- `requirement.txt`: This archive contains part of dependencies are required. In case you aren't using a environment manager, make sure use: `pip install -r requirements.txt` to set some dependencies.

- `environment.yml`: Contain all dependencies and channels that are required.

- `Makefile` This is the main archive used to configure conda environment.

## Configuring conda environment:
    ```
    $ make setup
    ```
- Use the comand above to create a new configured conda environmet or update if it has already created. After that, use the follow comand: `  conda activate vladmir` to activate the environment.

    ```
    $ make tools
    ```
    - Install sra-toolkit and jellyfish. Before, make sure you are in vladmir activated environment 

    



