# Gilead\_follow\_up\_email\_question

Hello folks,

For our internal process, we created the diagram below\. The diagram is high\-level and only takes into account end users \(i\.e\., no admin user flow is included\)\. Can you please review the diagram and confirm if it's accurate? Additionally, can you help us with the following questions:

1. Is there any front\-end layer before the \.NET cluster? \(e\.g\., a React or Vue app\)

    1. 3\.5\.0 前端和后端合成一个镜像

    2. Vue 框架来写网页

2. What are the use cases in which users will use async compute \(Rabbit MQ\)? What about synchronous compute \(API\)?

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZTFlYTc5MzE3MzVkYTc5NTJiYjUzYjg5MWJmMTA3OGNfNGQxOGY1N2VhNjEzNjkzZmI0YTEyZTAxZjAzZjQwNzhfSUQ6NzU3NzYzMDQyMjQ5NTMzMzU5OF8xNzkwMTkyMjc0OjE3OTAyNzg2NzRfVjM)

\`\`\`

My actual email response \(sent on Dec 1, 2025\)

1. The high\-level diagram is largely accurate, with one minor correction: the "\.Net Core web cluster" component also needs to connect to AWS RDS\. 

2. Regarding the front\-end layer before the \.Net cluster, yes \- we use the Vue framework 

3. Asynchronous compute is handled via RabbitMQ, and typical use cases include retrosynthesis route search, forward synthesis, GPU\-accelerated similarity search, and deep\-learning model inference\.  Synchronous compute is used for fast operations that can finish within a normal HTTP response time, such as loading pages, project lists, saved tasks, routes, and reports, as well as lightweight calculations including condition optimization and basic searches\. 

\`\`\`



My answer:

###### **Can you please review the diagram and confirm if it's accurate? **

The high\-level diagram is largely accurate but I'd note a few clarifications: 

**NET Core web cluster也要访问rds 数据库**

- ~~RabbitMQ handles asynchronous processing requests to Java algorithm services but it's bidirectional\.  After computation, Java Algorithm Groups publish the results/status back to RabbitMQ\. API layer listens on a queue to receive information \(e\.g\., task progress, task completion, etc\)~~

- ~~RabbitMQ 有两个队列，一个是上传任务，一个获得结果~~

###### **Is there any front\-end layer before the \.NET cluster? \(e\.g\., a React or Vue app\)**

1. **Vue app**

No separate front\-end service is shown in front of the \.NET Core web cluster\.

So: no dedicated React/Vue front\-end service in front of the \.NET cluster; the \.NET Core web apps are the front\-end\.

###### **What are the use cases in which users will use async compute \(Rabbit MQ\)? What about synchronous compute \(API\)?**

#### Async compute \(via RabbitMQ\)

**RabbitMQ is used for long\-running, heavy, or batch computations that shouldn’t block the user’s HTTP request\. Typical cases:**

- Retrosynthesis route search and complex route expansion

- Forward synthesis / virtual enumeration that touches large chemical spaces

- GPU\-accelerated similarity search or deep\-learning models \(via the GPU Service\)

- Condition optimization, impurity prediction, process search, or other algorithm\-heavy workflows

Flow:
 Browser → \.NET Core web cluster → REST API → enqueue task in RabbitMQ → Java Algorithm Groups / GPU Service process asynchronously → results stored \(DB / cache\) → UI polls or refreshes to show results\.

#### Synchronous compute \(direct API\)

条件优化，条件搜索

**Synchronous compute is used for fast operations that can finish within a normal HTTP response time, e\.g\.:**

- Loading pages, project lists, saved tasks, routes, and reports

- Simple lookups or filters on already computed results

- User/profile/permission queries

- Lightweight calculations or validations that complete in milliseconds–seconds

Flow:

Browser → \.NET Core web cluster → REST API → compute directly \(or quick call to Java service / DB\) → return response immediately\.





###### **Are Chemical\.AI's APIs exposed to end users? Do users only have access to the user interface \(Vue app\)?**

Yes\. Chemical\.AI’s APIs are available to end users, but they are protected by strict security controls\. By default, API access is disabled and must be explicitly activated\. Enabling API access requires a separate application process and involves additional licensing or purchase conditions\.



###### I**s there an average size for user input \(chemical molecules\)?**

There is no fixed molecule\-size limitation for user inputs\. The platform supports a wide range of molecular sizes and structural complexities\.

###### **Regarding the different applications for synchronous and asynchronous compute, based on what you said, can I assume the following:**

1. New chemical route requests are queued for processing\. Some endpoints \(e\.g\. for data upload and results retrieval\) are real time\. New chemical routes requests are managed via RabbitMQ, and the request and associated data are processed asynchronously\. This enables the system to process data in parallel and at high throughput, improving scalability and reducing latency\.

Yes, this is correct\. 

###### **What resources/components of Chemical\.AI are facing public internet and what are in a private network / VPC? Are storage resources / databases facing public internet?**

Only the web frontend is exposed to the public internet—specifically via HTTPS on ports 80/443 \(with port 80 redirecting to 443\)\. All backend components operate exclusively inside a private network or VPC\. These include: backend microservices, databases, storage resources, RabbitMQ, Redis, and monitoring systems\. 

###### **Do you have any security architecture documentation/diagram that could be shared with us? For example, describing which security tools / encryption are applied in each route or component\.**

We do not currently maintain a formally published security architecture document\. However, I have prepared a set of screenshots that illustrate some of the security controls\. 

