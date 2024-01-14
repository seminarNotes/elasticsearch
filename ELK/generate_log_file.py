import os
import shutil
import random
import numpy as np
from datetime import datetime
from datetime import timedelta
from datetime import time as time_object

def generate_log_line(timestamp):
    # Define log components
    loglevels_weight = [4, 60, 25, 10, 1]

    loglevels = ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
    
    threads = ["main",
               "http-nio-8080-exec-1",
               "background-thread",
               "scheduler-1",
               "scheduler-2",
               "worker-1",
               "worker-2",
               "request-handler-1",
               "request-handler-2",
               "task-executor-1",
               "api-request-1",
               "api-request-2",
               "database-query-1",
               "database-query-2",
               "email-sender-1",
               "email-sender-2",
               "logging-thread-1",
               "logging-thread-2",
               "notification-service-1",
               "notification-service-2"
               ]
    
    classes = ["com.example.app",
               "com.example.service",
               "com.example.controller",
               "com.example.model",
               "com.example.util",
               "com.example.repository",
               "com.example.config",
               "com.example.security",
               "com.example.web",
               "com.example.messaging", 
               "com.example.validation", 
               "com.example.exception", 
               "com.example.dao", 
               "com.example.dto", 
               "com.example.handler", 
               "com.example.scheduler", 
               "com.example.listener", 
               "com.example.aspect", 
               "com.example.transformer", 
               "com.example.logger"
               ]
    
    files = ["DatabaseConnection.java", 
             "UserService.java", 
             "HomeController.java", 
             "ProductController.java", 
             "DatabaseUtil.java", 
             "FileParser.java", 
             "EmailSender.java", 
             "SecurityConfig.java", 
             "MessageListener.java", 
             "ValidationUtil.java", 
             "ExceptionHandling.java", 
             "DataAccessObject.java", 
             "UserDTO.java", 
             "LoggingHandler.java", 
             "TaskScheduler.java", 
             "EventListener.java", 
             "LoggingAspect.java", 
             "DataTransformer.java", 
             "FileLogger.java", 
             "NotificationService.java"
             ]

    messages = {
    'DEBUG': [
        'Debugging information: Step 1',
        'Debug log entry: Operation started',
        'Debug message: Verifying input data',
        'Debugging in progress: Module A',
        'Debugging complete: No errors found'
        ],
    'INFO': [
        'Connection established successfully',
        'User data retrieved',
        'Product added to cart',
        'Payment processing in progress',
        'File uploaded successfully',
        'Authentication successful',
        'Data synchronization complete',
        'Email sent successfully',
        'Data backup completed',
        'Log file archived',
        'Successful login from a new device'
        ],
    'WARN': [
        'Task completed with warnings',
        'Permission denied: Access denied',
        'Resource not available',
        'Network error: Connection lost',
        'Invalid credentials provided'
        ],
    'ERROR': [
        'Database connection failed: Timeout expired',
        'Null pointer exception in user processing',
        'Server error: Internal server error',
        'Payment failed: Insufficient funds',
        'User session expired',
        'File download started',
        'Service unavailable: Server maintenance',
        'File not found in the directory',
        'Security breach detected: Unauthorized access'
    ],
    'FATAL': [
        'Critical error: Application crash',
        'Another critical error occurred',
        'System failure: Unable to recover',
        'Fatal error: Data corruption detected',
        'Emergency: System shutdown required'
        ]
    }
    if False :
        """grok 패턴을 이용하여, 다양한 로그 파일을 생성할 수 있음
        generate_log_line(timestamp, pattern)와 같이 함수 input를 조정해야 함
        해당 부분은 추후 구현 예정"""
        pattern = None
        
        if pattern == 'web_server_log':
            """웹 서버 로그
            \[%{TIMESTAMP_ISO8601:timestamp}\] "%{WORD:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:httpversion}" %{NUMBER:response_code} %{NUMBER:response_size} "-" "%{GREEDYDATA:user_agent}"
            TIMESTAMP_ISO8601: 타임스탬프
            WORD: HTTP 메소드 (GET, POST 등)
            URIPATHPARAM: 요청된 URI 및 파라미터
            NUMBER: HTTP 버전, 응답 코드, 응답 크기
            GREEDYDATA: 사용자 에이전트"""
            methods = ["GET", "POST"]
            uris = ["/index.html", "/contact"]
            http_version = "1.1"
            response_code = random.choice([200, 404, 500])
            response_size = random.randint(100, 10000)
            user_agent = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
            log_line = f'[{timestamp}] "{random.choice(methods)} {random.choice(uris)} HTTP/{http_version}" {response_code} {response_size} "-" "{user_agent}"'
        elif pattern == 'program_log':
            """프로그램 로그
            %{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:loglevel} \[%{DATA:thread}\] %{JAVACLASS:class} \(%{JAVAFILE:file}:%{NUMBER:line}\) - %{GREEDYDATA:message}
            TIMESTAMP_ISO8601: 타임스탬프
            LOGLEVEL: 로그 레벨 (ERROR 등)
            DATA: 스레드 이름
            JAVACLASS: 클래스 이름
            JAVAFILE: 자바 파일 이름
            NUMBER: 라인 번호
            GREEDYDATA: 로그 메시지"""
            log_line = f"{timestamp} {random.choice(loglevels)} [{random.choice(threads)}] {random.choice(classes)} ({random.choice(files)}:{random.randint(1, 100)}) - {random.choice(messages)}"
        elif pattern == 'system_log':
            """시스템 로그
            %{SYSLOGTIMESTAMP:timestamp} %{HOSTNAME:host} %{DATA:process}: \[%{NUMBER:pid}\] %{GREEDYDATA:message}
            SYSLOGTIMESTAMP: 타임스탬프
            HOSTNAME: 호스트 이름
            DATA: 프로세스 이름
            NUMBER: 프로세스 ID
            GREEDYDATA: 로그 메시지"""
            process = "kernel"
            pid = random.randint(1000, 9999)
            message = "CPU temperature above threshold, cpu clock throttled"
            log_line = f"{timestamp} myserver {process}: [{pid}] {message}"
        elif pattern == 'security_log':
            """보안 로그
            %{SYSLOGTIMESTAMP:timestamp} %{HOSTNAME:host} %{DATA:process}\[%{NUMBER:pid}\]: %{GREEDYDATA:message}
            SYSLOGTIMESTAMP: 타임스탬프
            HOSTNAME: 호스트 이름
            DATA: 프로세스 이름
            NUMBER: 프로세스 ID
            GREEDYDATA: 로그 메시지"""
            process = "sshd"
            pid = random.randint(1000, 9999)
            message = "Failed password for invalid user admin from 192.168.1.10 port 22 ssh2"
            log_line = f"{timestamp} myserver {process}[{pid}]: {message}"
        elif pattern == 'debug_log':
            """디버그 로그
            %{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:loglevel} \[%{DATA:thread}\] %{JAVACLASS:class} \(%{JAVAFILE:file}:%{NUMBER:line}) - %{GREEDYDATA:message}
            `TIMESTAMP_ISO8601`: 타임스탬프
            - `LOGLEVEL`: 로그 레벨 (DEBUG 등)
            - `DATA`: 스레드 이름
            - `JAVACLASS`: 클래스 이름
            - `JAVAFILE`: 자바 파일 이름
            - `NUMBER`: 라인 번호
            - `GREEDYDATA`: 로그 메시지"""
            log_line = f"{timestamp} DEBUG [{random.choice(threads)}] {random.choice(classes)} ({random.choice(files)}:{random.randint(1, 100)}) - Fetching user details for userId: 42"
        else:
            log_line = "Unknown pattern"
            return None

 
    sampled_loglevel = random.choices(loglevels,
                                     weights = list(np.array(loglevels_weight) / sum(loglevels_weight))
                                     )[0]
    sampled_thread = random.choice(threads)
    sampled_class = random.choice(classes)
    sampled_file = random.choice(files)
    sampled_line = random.randint(1, 500)
    sampled_message = random.choice(messages[sampled_loglevel])

    # 특정 시간대 데이터 베이스에 대한 에러 반영
    if datetime.strptime(timestamp.split(",")[0], "%Y-%m-%d %H:%M:%S").time() > time_object(1,00,00) and \
        datetime.strptime(timestamp.split(",")[0], "%Y-%m-%d %H:%M:%S").time() > time_object(5,30,00) :
        if random.random() < 0.1 :
            sampled_file = "DatabaseConnection.java"
            sampled_loglevel = "ERROR"
            sampled_message = random.choice(messages[sampled_loglevel])
        
        elif random.random() < 0.05 :
            sampled_file = "DatabaseConnection.java"
            sampled_loglevel = "FATAL"
            sampled_message = random.choice(messages[sampled_loglevel])

    
    # 특정 시간대 접속 유저가 많은 것을 반영
    elif datetime.strptime(timestamp.split(",")[0], "%Y-%m-%d %H:%M:%S").time() > time_object(13,00,00) and \
        datetime.strptime(timestamp.split(",")[0], "%Y-%m-%d %H:%M:%S").time() > time_object(17,30,00) :
        if random.random() < 0.2 :
            sampled_file = "UserService.java"
            sampled_loglevel = "INFO"
            sampled_message = random.choice(messages[sampled_loglevel])
        
        elif random.random() < 0.2 :
            sampled_file = "UserService.java"
            sampled_loglevel = "WARNING"
            sampled_message = random.choice(messages[sampled_loglevel])
        
        elif random.random() < 0.1 :
            sampled_file = "UserService.java"
            sampled_loglevel = "ERROR"
            sampled_message = random.choice(messages[sampled_loglevel])

    log_line = f"{timestamp} {sampled_loglevel} [{sampled_thread}] {sampled_class} ({sampled_file}:{sampled_line}) - {sampled_message}"
    return log_line

def create_log_file(basedate_str, num_lines = 500):
    basedate = datetime.strptime(basedate_str, "%Y%m%d")
    log_lines = []

    for i in range(num_lines):
        weight00to06 = [3, 4, 5, 5, 4, 3]
        weight07to12 = [1, 1, 1, 3, 4, 5]
        weight13to18 = [6, 6, 5, 4, 3, 1]
        weight19to24 = [1, 1, 1, 1, 1, 1]

        weight = weight00to06 + weight07to12 + weight13to18 + weight19to24
        hour_weight = list(np.array(weight) / sum(weight))

        sampled_hour = random.choices(range(24), weights = hour_weight)[0]
        sampled_minute = random.randint(0, 59)
        sampled_second = random.randint(0, 59)

        timestamp = datetime(basedate.year,
                             basedate.month,
                             basedate.day,
                             sampled_hour,
                             sampled_minute,
                             sampled_second
                             )

        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        
        log_line = generate_log_line(formatted_timestamp)
        log_lines.append(log_line)

    # Sort log lines
    log_lines.sort()

    PATH_WINDOWS = os.getcwd().split('\\')

    PATH_PYTION = r''
    for ii in range(len(PATH_WINDOWS)) :
        PATH_PYTION += str(PATH_WINDOWS[ii] + r'/') 
    
    PATH_PYTION += r"logs/"
    
    formatted_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    if os.path.exists(PATH_PYTION + f"log_{basedate_str}.log") :
        shutil.move(PATH_PYTION + f"log_{basedate_str}.log",
                    PATH_PYTION + f"log_{basedate_str}" + formatted_datetime + r".log")

    # Save log lines to a file
    file_name = PATH_PYTION + f"log_{basedate_str}.log"
    with open(file_name, 'w') as file:
        for line in log_lines:
            file.write(line + "\n")
    
    return file_name

# Example usage
if __name__ == "__main__":

    basedate_str = "20240113"
    log_file_name = create_log_file(basedate_str, 50000)
    print(f"Log file created: {log_file_name}")
