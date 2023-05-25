-- REMOVE TABLES

DROP TABLE IF EXISTS parcel CASCADE;
DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS sale CASCADE;
DROP TABLE IF EXISTS supplier CASCADE;
DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS eanproduct CASCADE;
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS department CASCADE;
DROP TABLE IF EXISTS workplace CASCADE;
DROP TABLE IF EXISTS office CASCADE;
DROP TABLE IF EXISTS warehouse CASCADE;
DROP TABLE IF EXISTS pay CASCADE;
DROP TABLE IF EXISTS has CASCADE;
DROP TABLE IF EXISTS process CASCADE;
DROP TABLE IF EXISTS works CASCADE;
DROP TABLE IF EXISTS delivery CASCADE;

-- ENTITIES

CREATE TABLE customer (
    cust_no     SERIAL,
    cust_name   VARCHAR(80) NOT NULL,
    email       VARCHAR(254),
    phone       VARCHAR(15) NOT NULL,
    cust_add    VARCHAR(255) NOT NULL,
    PRIMARY KEY(cust_no),   
    UNIQUE(email),
    CHECK(LENGTH(email) > 5),
    CHECK(LENGTH(phone) > 2)
);

CREATE TABLE parcel ( 
    --!! Order cannot be used as table name !!
    order_no    SERIAL,
    order_date  DATE NOT NULL,
    cust_no     INTEGER,    -- Arbitrary number based on world population
    PRIMARY KEY(order_no),
    FOREIGN KEY(cust_no) REFERENCES customer(cust_no)
    -- IC-1: Every order must exist in the table 'contains'
);

CREATE TABLE sale (
    order_no    INTEGER,
    PRIMARY KEY(order_no),
    FOREIGN KEY(order_no) REFERENCES parcel
);

CREATE TABLE product (
    sku         VARCHAR(12),
    prod_name   VARCHAR(80) NOT NULL,
    prod_desc   VARCHAR(1000) NOT NULL, -- Arbitrary size for long product description
    price       NUMERIC(16,4) NOT NULL,
    PRIMARY KEY(sku),
    CHECK (LENGTH(sku) > 7)
    --IC-2: Every product must exist in the table 'suplier'
);

CREATE TABLE eanproduct (
    sku         VARCHAR(12), 
    ean         VARCHAR(13) NOT NULL,   -- Most widely used EAN code, the first two or three digits represent the country code or GS1 prefix, followed by the manufacturer code, the product code, and the final digit, which is a check digit for error detection.
    PRIMARY KEY(sku),
    FOREIGN KEY(sku) REFERENCES product(sku),
    CHECK (LENGTH(sku) > 7),
    CHECK (ean LIKE 'GS1__________')
);

CREATE TABLE supplier (
    tin             VARCHAR(12),    -- We assume suppliers are all legal entities, therefor TINs are the follow format XXXXXXXXX-YY
    supp_name       VARCHAR(80) NOT NULL,
    supp_add        VARCHAR(255) NOT NULL,
    contract_date   DATE NOT NULL,
    sku             VARCHAR(12),
    PRIMARY KEY(tin),
    FOREIGN KEY(sku) REFERENCES product(sku),
    CHECK (LENGTH(sku) > 7),
    CHECK (tin LIKE '_________-__')
);

CREATE TABLE employee(
    ssn         VARCHAR(11),    -- Based on USA's SSN, with the following layout XXX-XX-XXXX
    tin         VARCHAR(9),     -- Based on Portugal's NIF, having only 9 digits
    bdate       DATE NOT NULL,
    emp_name    VARCHAR(80) NOT NULL,
    PRIMARY KEY(ssn),
    UNIQUE(tin),
    CHECK (LENGTH(tin) = 9),
    CHECK (ssn LIKE '___-__-____')
    -- IC-3: Every emplyee must exist in the table 'works'
);

CREATE TABLE department(
    dep_name    VARCHAR(200),
    PRIMARY KEY(dep_name)
);

CREATE TABLE workplace(
    work_add    VARCHAR(255),
    lat         NUMERIC(8,6),
    long        NUMERIC(9,6),
    PRIMARY KEY(work_add),
    UNIQUE(lat,long)
);

CREATE TABLE office(
    work_add    VARCHAR(255),
    PRIMARY KEY(work_add),
    FOREIGN KEY(work_add) REFERENCES workplace(work_add)
);

CREATE TABLE warehouse(
    work_add    VARCHAR(255),
    PRIMARY KEY(work_add),
    FOREIGN KEY(work_add) REFERENCES workplace(work_add)
);

-- ASSOCIATIONS

CREATE TABLE pay (
    cust_no     INTEGER,
    order_no    INTEGER,
    PRIMARY KEY(order_no),
    FOREIGN KEY(cust_no) REFERENCES customer(cust_no),
    FOREIGN KEY(order_no) REFERENCES sale(order_no)
);

CREATE TABLE has (
    --!! Contains cannot be used as a table name !!
    order_no    INTEGER,
    sku         VARCHAR(12),
    qty         INTEGER NOT NULL,
    PRIMARY KEY(order_no, sku),
    FOREIGN KEY(order_no) REFERENCES parcel(order_no),
    FOREIGN KEY(sku) REFERENCES product(sku),
    CHECK (LENGTH(sku) > 7)
);

CREATE TABLE process (
    order_no    INTEGER,
    ssn         VARCHAR(11),
    PRIMARY KEY(order_no, ssn),
    FOREIGN KEY(order_no) REFERENCES parcel(order_no),
    FOREIGN KEY(ssn) REFERENCES employee(ssn),
    CHECK (ssn LIKE '___-__-____')
);

CREATE TABLE works (
    ssn         VARCHAR(11),
    dep_name    VARCHAR(200),
    work_add    VARCHAR(255),
    PRIMARY KEY(ssn, dep_name, work_add),
    FOREIGN KEY(ssn) REFERENCES employee(ssn),
    FOREIGN KEY(dep_name) REFERENCES department(dep_name),
    FOREIGN KEY(work_add) REFERENCES workplace(work_add),
    CHECK (ssn LIKE '___-__-____')
);

CREATE TABLE delivery (
    work_add    VARCHAR(255),
    sku         VARCHAR(12),
    tin         VARCHAR(12),
    PRIMARY KEY(work_add, sku, tin),
    FOREIGN KEY(work_add) REFERENCES warehouse(work_add),
    FOREIGN KEY(sku) REFERENCES product(sku),
    FOREIGN KEY(tin) REFERENCES supplier(tin),
    CHECK (LENGTH(sku) > 7),
    CHECK (LENGTH(tin) > 8)
);