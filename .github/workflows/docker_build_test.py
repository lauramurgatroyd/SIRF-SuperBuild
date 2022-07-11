name: Docker build test publish

on:
  pull_request:
    branches: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install docker and pre-reqs
        shell: bash -l {0}
        run: |
          sudo apt-get update -y
          sudo apt-get upgrade -y
          sudo apt-get install ca-certificates curl gnupg lsb-release -y
          sudo mkdir -p /etc/apt/keyrings
          curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
          echo \
            "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
            $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
          sudo apt-get update
          sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
          sudo docker run hello-world

      - name: Build docker container
        shell: bash -l {0}
        run: |
          docker build docker

#       - name: Run docker container with tests
#         shell: bash -l {0}
#         run: |
#           docker run --rm --entrypoint /bin/bash -v /home/runner/work/CILViewer/CILViewer:/root/source_code  cil-viewer -c "source ./mambaforge/etc/profile.d/conda.sh && conda activate cilviewer_webapp && conda install cil-data pytest -c ccpi && python -m pytest /root/source_code/Wrappers/Python -k 'not test_version'"
#     # TODO: publish to come later
