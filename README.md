# 前置作業
Shell Editor 預設啟用的Terminal是不會binding project的。

如果大家有個慣用Project，建議可以在CloudShell內更新`.bashrc` 檔案

`vim ~/.bashrc`

在最下方的部分加入
gcloud config set project [YOUR_CORRECT_PROJECT_ID]

# Step1 - gsutil 展示
使用命令列操作gloud storage

```
# 瀏覽所有Bucket
gsutil ls

# 瀏覽指定Bucket內的object
gsutil ls $BUCKET_NAME

# 上傳物件至Bucket
gsutil cp SOURCE_FILE DESTINATION

# 下載物件回本地端
gsutil cp DESTINATION SOURCE_FILE

# 刪除物件
gsutil rm OBJECT_PATH

```

# Step2 使用Python在Cloud Shell Editor 開發 HTTP SERVER

關於Python, 目前Cloud shell 僅支援Virtual Env以及  Requirement


```
# 安裝環境，不探討套件管理環境
pip3 install -r requirements.txt

```

逐步執行 step2, step3, step4


# 放到GCE上，連入測試安裝可行性

使用Debian image

```
sudo apt-get install -y python3-pip
sudo apt-get install -y git 
git clone https://github.com/BingHongLi/gcp-basic-demo.git
cd gcp-basic-demo
pip3 install -r requirements.txt
python3 step4_integrate_both.py
```

# 使用docker

連入，並安裝docker

```
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io

sudo usermod -aG docker $USER

git clone https://github.com/BingHongLi/gcp-basic-demo.git

'''

因為安裝docker，故必須重新登入

'''

cd gcp-basic-demo

docker build -t flask-gcp-gs .

docker run -p 80:8081  -d flask-gcp-gs

```