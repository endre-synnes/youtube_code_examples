# Lambda and Serverless Aurora

### SQL queries
create table:
```SQL
create table birds(
  id VARCHAR(100) NOT NULL,
  name VARCHAR(50) NOT NULL,
  canFly BOOL,
  PRIMARY KEY (id)
)
```

insert bird object:
```SQL
insert into birds(id, name, canFly) values("1001", "Eagle", true)
```

get all from birds table:
```SQL
select * from birds
```
