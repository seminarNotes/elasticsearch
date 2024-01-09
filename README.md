# ElasticSearch Setup 
최초 작성일 : 2023-12-27  
마지막 수정일 : 2024-01-09
  
## 0. Overview
Elasticsearch는 NosSQL 데이터를 저장하고, 조회(검색)할 수 있는 아파치 재단의 루씬(Lucence)을 기반으로 개발된 오픈 소스 검색 엔진이다. 관계형 데이터 베이스와 비교하였을 때, 사용하는 용어와 구조가 다르기 때문에 대표적인 개념을 잠시 정리한다. Elasticsearch 내 다양한 object와 관계형 데이터 베이스(RDBMS)에서의 개념은 다음과 같이 대응된다.

|ElasticSearch|RDBMS|
|---|---|
|인덱스(Index)|데이터베이스(DB)|
|샤드|파티션|
|타입(Type)|테이블|
|문서|행|
|필드|열|
|매핑|스키마|
|Query DSL|SQL|




## Table of Contents
1. [Step up elasticsearch and kibana](#1.-Step-up-elasticsearch-and-kibana)
2. [Execute_ElasticSearch](#2.-Execute-ElasticSearch)


## 1. Step up elasticsearch and kibana
Windows 환경에서 ElasticSearch를 설치하고, 세팅하는 과정을 기록한다.

ElasticSearch
ElasticSearch를 실행하기 위해서 ElasticSearch와 함께 Kibana를 설치해야 한다. Kibana는 ElasticSearch를 사용할 때, 대시보드를 사용할 수 있도록 GUI를 제공하는 소프트웨어다. 각 소프트웨어의 설치 파일은 아래에서 다운로드 할 수 있다.
```console
https://www.elastic.co/kr/downloads/elasticsearch
```

```console
https://www.elastic.co/kr/downloads/kibana
```

다운로드 이후, 작업 디렉토리에서 압축 파일을 푼다. 예를 들어, C드라이브 아래 작업 디렉토리(ELK, Elasticsearch, Logstash, Kibana의 줄임말)를 생성하고, zip 파일을 옮긴 후, 압축 파일을 푼다.

C:\ELK

참고로, 개발 및 환경을 세팅할 때, 경로에는 "한글"과 version을 나타내는 "x.x.x"과 같은 폴더/파일 이름은 생략하는 것을 강력히 권장한다. 필자는 elasticsearch와 kibana가 설치된 폴더의 경로를 아래와 같도록, 폴더 명을 각각 변경하였다.

C:\ELK\elasticsearch

C:\ELK\kibana

Visual Studio Code를 이용해서 설치를 완료한다. 명령 프롬포트를 실행해서 작업 디렉토리를 열고(최상위 폴더를 ELK로 하고), Visual Stuido Code를 실행한다.
```console
C:\Users\seminarNotes>CD C:\ELK

C:\ELK>code .
```
Visual Studio Code와 함께 왼쪽 Explorer를 이용해서 elasticsearch.yml파일를 연다.
C:\ELK\elasticsearch\config\elasticsearch.yml

그리고 아래와 같은 문구를 추가한다.
```yaml
#config/elasticsearch.yml
cluster.name: cluster-test
node.name: cluster-test-node01

path:
  data: C:\ELK\elasticsearch\data
  logs: C:\ELK\elasticsearch\logs  

network.host: 127.0.0.1

discovery.type: "single-node"
xpack.security.enabled: false
```

다음으로 C:\ITStudy\ELK\elasticsearch\config\jvm.options 파일에 접속해서, -Xms5g/-Xmx5g의 부분의 주석을 해제하고, -Xms1g/-Xmx1g로 변경한다. 


```
## -Xms5g
## -Xmx5g
```

```
-Xms1g
-Xmx1g
```

해당 수정 부분은 elasticsearch를 사용할 때, 할당하는 메모리에 대한 세팅으로, 메모리에 대한 여유가 있는 유저는 -Xms5g/-Xmx5g 그대로 사용해도 무방하다.

또, C:\ITStudy\ELK\kibana\config\kibana.yml 파일에 접속하여, 맨 아래 아래와 같은 세팅값을 추가한다.

```yaml
#config/kibana.yml
server.port: 5601
server.host: localhost
server.publicBaseUrl: "http://localhost:5601"
elasticsearch.hosts: ["http://localhost:9200"]
```

설치된 elasticsearch와 kibana는 아래 batch파일을 터미널을 통해 실행한다.
```console
c:\ELK\elasticsearch\bin\elasticsearch.bat

c:\ELK\kibana\bin\kibana.bat
```
설치와 실행을 점검하기 위해, elaticsearch는 http://localhost:9200 kibana는 http://localhost:5601 에 접속해서 확인한다.


## 2. Elastic 실행

ElasticSearch에서 하나의 인덱스에 하나의 타입만 구성할 수 있다. 그리고 HTTP를 통해 JSON 형식의 Restful API를 사용한다. 이 때, Restful API는 HTTP 헤더와 URL만 사용하여 다양한 형태의 요청을 할 수 있는 HTTP 프로토콜을 최대한 활용하도록 고안된 아키텍쳐를 의미한다. 사용되는 쿼리(Query DSL)은 다음 표와 같다.
|요청 쿼리|기능|
|---|---|
|GET|데이터 조회|
|PUT, PATCH(일부 수정)|데이터 생성|
|POST|인덱스 업데이트, 데이터 조회|
|DELETE|인덱스 데이터 삭제|
|HEAD|인덱스의 정보 확인|


## 4. log 수집

C:\ITStudy\ELK\server1\script1.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/subpage1')
def deposit():
    return 'subpage1'

@app.route('/subpage2')
def withdraw():
    return 'subpage2'

if __name__ == '__main__':
    app.run("0.0.0.0", port=5001, debug=True)
```

C:\ELK\server1\filebeat\filebeat.yml

```yml

filebeat:
  inputs:
    - type: log
      enabled: true
      paths:
        - C:/ELK/server1/script1.log
output.logstash:
  hosts: ["localhost:5044"]
```




C:\ELK\logstash\config\logstash-from-server1.conf

```conf
input {
    beats {
        port => 5044
    }
}

filter {
    grok {
        match => { "message" => '%{IP:client_ip} - - \[%{GREEDYDATA:timestamp}\] "%{WORD:http_method} %{URIPATH:request_path} HTTP/%{NUMBER:http_version}" %{NUMBER:response_code} -'
}
    }

    mutate {
        remove_field => ["host", "@version", "message", "agent", "log"]
    }
}

output {
  elasticsearch {
    hosts => "http://127.0.0.1:9200"
    # index => "logs-server1-%{+YYYY.MM.dd}"
	index => "logs-server"
    data_stream => false
    action => "create"
  }
  stdout {}
}
```

