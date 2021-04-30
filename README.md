# Discounts in 1

### Links
Top area are general information of whole project, you may be interest in [Database Focus](https://github.com/RPLapple/2021discount/blob/master/README.md#database-focus) or [CI/CD Focus](https://github.com/RPLapple/2021discount/blob/master/README.md#cicd-focus).


**Target Reader**<br>
Anyone who interest in learning to code.

**Aim**<br>
To provide a simple guide to the very beginner a basic CI/CD process

**Experience level**<br>
Beginner (one person project)

**Softwares**<br>
Python, SQLite, Django, Github, CircleCI, Google Cloud Platform (GCP)

## Introduction and Overview<br>
Discounts in 1, is an application for gathering different weekly supermarket discounts into 1 site. It will contain the discount price and percentage information for users. If the user joins as a member, the application will provide extra functions, credit card and rewards app (e.g. payback), to help users save more money.

## The software you will use in this project<br>
This application developed with the below resources. There are many software and framework you can choose from, but here only provide 1 type of instruction.

**Frontend** <br>
we use a free template from the "Mashup Templates" website. It contains HTML, CSS, and Javascript.

**Backend** <br>
Django, Python's libs, is a very powerful framework, it has multifunction to help us from automated testing, database, connecting frontend and backend also to deploy to the cloud system.

**Repository** <br>
Github is the repository for code hosting platform for version control and collaboration.

**CI/CD** <br>
CircleCI, is a continuous integration and continuous delivery platform, can connect Github and automatically deploy to cloud system with pre-build software docker.

**Could system** <br>
Google Cloud Platform, if you want to build and run an application to reach users worldwide, or to utilize massive data storage but with elasticity capacity, without building and maintain a physical machine, to have a cloud system is a great idea.

## Development environment through version control to their production environment

**1.Different engineer working on the same project** <br>
Usually, a project is built by many engineers. They use the same repository to upload and merge their code for the git branching model, production, staging, and master, until the final version of the product.

**2. Github push to circleCI automatically**<br>
We need to set the circleCI to connect to a specific branch from the Github repository. Once the chosen branch been merged and approved, it will integrate automatically by circleCI to build and test the application. (CI, Continues integration)

**3. CircleCI deploy data to GCP storage**<br>
When the CI process finished, it will automatically deploy to GCP storage.

**4. Notify the post to succeed or not**<br>
**5. Notify build succeed or not** <br>
No. 4 and 5, CircleCI record each process and how much time they have used. If there's a bug, you can find error information easily.

**6. Client request browser information to API (App Engine)**<br>
When a user browsing a website, it will request from the cloud API (app engine), usually it should be a server to take the request, but django framework has pre-build function to connect it.

**7. API (App Engine) request data from Cloud SQL**<br>
After API receives the request, it will request from its database, cloud SQL.

**8. Cloud SQL provide data to API (App Engine)**<br>
Once the storage found the data, it will response to the API

**9. API (App Engine) provide information to client**<br>
API will response to the client with the final result.

<img src="picsForReadme/全圖.png" width="425" alt="all"/> <br>


## Database Focus
### [Principles of relational database management systems](https://en.wikipedia.org/wiki/Relational_database) <br>
A relational database means each data will be stored in a field and combined into a table. After all these tables connect to each other, it became a database. It also using a specific database language, [SQL]([https://en.wikipedia.org/wiki/SQL](https://en.wikipedia.org/wiki/SQL)) [The most popular SQL in 2020]([https://learnsql.com/blog/most-popular-sql-databases-2020/](https://learnsql.com/blog/most-popular-sql-databases-2020/)) are Mysql, PostgreSQL, SQLite, Microsoft SQL Server. Usually, people follow [E.F. Codd’s 12 Rules for RDBMS]([https://www.tutorialspoint.com/e-f-codd-s-12-rules-for-rdbms](https://www.tutorialspoint.com/e-f-codd-s-12-rules-for-rdbms)) standards to create a database. <br>
<br>
Due to this is a small project, I used pre-build database SQLite in Django. It is a light version database, already has built-in functions which suit for a small and not complex project. <br>
<br>
### [Entity-relationship models](https://en.wikipedia.org/wiki/Entity–relationship_model) <br>
An entity is a thing that exists either physically or logically. For example, this project has a product (physically exist), but a member point would be a concept (logically exist). Usually, we discuss the projects with customers and designers first, to confirm the needs then create a real database.<br>
<br>


### [Database normalization and schema optimization](https://en.wikipedia.org/wiki/Database_normalization) <br>
Database normalization is the process of structuring a database, in accordance with a series of so-called normal forms in order to reduce data redundancy and improve integrity.<br>
In the present database, the most common normal form is 3NF. It was generally agreed that although having a higher normal form could binding the database better, but it also increases the complexity of data IO. Therefore, people tend to create functions with code to fix this issue. In this database, I tried <br>
- 1NF, each column has only 1 data and no repeat.<br>
- 2NF, meet the requirement of 1NF, move the partial dependency column to a different schema and use the Foreign Key to relate different tables.<br>
- 3NF, meet the requirement of 2NF, each column has no transitive dependency.<br>
<br>
<img src="picsForReadme/db01.png" width="425" alt="db01"/><br>
<img src="picsForReadme/db02.png" width="425" alt="db02"/><br>

### [Database indexing](https://en.wikipedia.org/wiki/Database_index) <br>

Database indexing could increase the searching speed. Because once it has Primary Key, it will turn to a [binary tree structure]([https://zhuanlan.zhihu.com/p/86189418](https://zhuanlan.zhihu.com/p/86189418)). This means if there are 1 billion data in a table, and we need only 1, usually, it will search 1 by 1 and the worst situation is, we need to look for it 1 billion times. If we turn this table into a binary try, it means this table will have to distinguish into different layers, it will reduce the searching times as the red path in the picture.<br>
![indexing]()<br>
<br>
But, due to the binary tree needs to maintain itself in correct status, even we changed only 1 small part, it will break its balance. So every time when a data has been changed, it will need to restructure again to keep everything in the right place.<br>

<img src="picsForReadme/binary tree.png" width="425" alt="bt"/><br>


### Object-relational mapper(ORM)frameworks.<br>
[An ORM framework is a programming technique for converting data between incompatible type systems using object-oriented programming languages](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping). It can hide the SQL into its logic, you only need to use simple language but can create the same table in the database. For example, Django is an ORM framework, if you want to create a product table in the database and contains a supermarket (FK), you only need to go to `models.py` and put<br>
<br>
'class Product(model.Model):
       supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)' 
But you can still execute SQL through the command-line interface, shell. <br>
<br>
<img src="picsForReadme/ORM.png" width="425" alt="ORM"/><br>


## CI/CD Focus

### How to connect to the GCP DB <br>
1. Connect to the DB, create an instance in GCP SQL, it may ask you to permit API. <br>
2. Select a suitable database zone <br>
<img src="picsForReadme/01SQL.png" height="560" alt="01SQL"/> <br>
3. Add the instance ID to setting.py (Django file) <br>
<img src="picsForReadme/02執行個體名稱.png" width="500" alt="02instance"/>
<img src="picsForReadme/03setting.png" width="500" alt="03setting"/> <br>

### How to connect to GCP <br>
1. To get the key from GCP
→ IAM & Admin → Service Account → Action → Manage Keys → Add Key <br>
<img src="picsForReadme/dp 01deploy get the key.png" width="500" alt="01key"/> <br>

2. Download the json file, copy the data and past into circleCI<br>
<img src="picsForReadme/dp 02circleCi 新增GCPKey那些.png" width="500" alt="02circleci"/> <br>

3. Enable the App Engine Admin API, so it got the permission to start. <br>
<img src="picsForReadme/dp 03 app engine api .png" width="500" alt="03appengine"/> <br>

4. Push the code to github again, and circleCI will build, test and deploy again.<br>
<img src="picsForReadme/dp 04 deploy成功的circleCI.png" width="500" alt="04circleciDeploy"/> <br>

5. Back to the CLI and run the gcloud. [How to change the project in GCP using CLI commands](https://ppt.cc/fFjzVx)<br>
Here fails was because I used another testing GCP account, but I changed to our university account now. For how to revise the data, we need to run 2 commands:<br>
`gcloud config set project projectID` and `gcloud components update`<br>
<img src="picsForReadme/dp 05 CLI deploy失敗.png" width="500" alt="05failCLI"/> <br>

6. Because here has an error said, that we need to make sure our email address has the [App Engine Deployer](https://ppt.cc/f3j7Px) role, so we need to back to IAM & Admin and set the permission. <br>
run `gcloud app deploy` again, everything went well and we can link to the target url.<br>
<img src="picsForReadme/dp 06 CLI deploy成功.png" width="500" alt="06successed"/> <br>
<img src="picsForReadme/dp 055 新增role:appengine.deployer人設.png" width="500" alt="055addRole"/> <br>

7. Here is the [final page](https://maximal-quanta-306619.ey.r.appspot.com/).<br>
<img src="picsForReadme/dp 07 final page onGCP.png" width="500" alt="07finalpage"/> <br>
