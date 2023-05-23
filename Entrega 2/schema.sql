-- REMOVE TABLES

DROP TABLE parcel;
DROP TABLE customer;
DROP TABLE sale;
DROP TABLE supplier;
DROP TABLE product;
DROP TABLE eanproduct;
DROP TABLE employee;
DROP TABLE department;
DROP TABLE workplace;
DROP TABLE office;
DROP TABLE warehouse;
DROP TABLE pay;
DROP TABLE has;
DROP TABLE process;
DROP TABLE works;
DROP TABLE deliver;

-- ENTITIES

CREATE TABLE parcel ( 
    --!! Order cannot be used as table name !!
    order_no    INTEGER(12),    -- Abitrary number, allowing up to one trillion orders
    order_date  DATE NOT NULL,
    cust_no     INTEGER(10),    -- Arbitrary number based on world population
    PRIMARY KEY(order_no),
    FOREIGN KEY(cust_no) REFERENCES customer(cust_no),
    CHECK (order_no > 0),
    CHECK (cust_no > 0),
    -- IC-1: Every order must exist in the table 'contains'
);

CREATE TABLE customer (
    cust_no     INTEGER(10),
    cust_name   VARCHAR(80) NOT NULL,
    email       VARCHAR(254),
    phone       VARCHAR(15) NOT NULL,
    cust_add    VARCHAR(255) NOT NULL,
    PRIMARY KEY(cust_no),
    UNIQUE(email),
    CHECK(email > 5),
    CHECK(phone > 2),
    CHECK (cust_no > 0),
);

CREATE TABLE sale (
    order_no    INTEGER(12),
    PRIMARY KEY(order_no),
    FOREIGN KEY(order_no) REFERENCES parcel(order_no),
    CHECK (order_no > 0),
);

CREATE TABLE product (
    sku         VARCHAR(12),
    prod_name   VARCHAR(80) NOT NULL,
    prod_desc   VARCHAR(1000) NOT NULL, -- Arbitrary size for long product description
    price       NUMERIC(16,4) NOT NULL,
    PRIMARY KEY(sku),
    CHECK (sku > 7),
    --IC-2: Every product must exist in the table 'suplier'
);

CREATE TABLE eanproduct (
    sku         VARCHAR(12), 
    ean         VARCHAR(13) NOT NULL,   -- Most widely used EAN code, the first two or three digits represent the country code or GS1 prefix, followed by the manufacturer code, the product code, and the final digit, which is a check digit for error detection.
    PRIMARY KEY(sku),
    FOREIGN KEY(sku) REFERENCES product(sku),
    CHECK (sku > 7),
    CHECK (ean = 'GS1__________'),
);

CREATE TABLE supplier (
    tin             VARCHAR(12),    -- We assume suppliers are all legal entities, therefor TINs are the follow format XXXXXXXXX-YY
    supp_name       VARCHAR(80) NOT NULL,
    supp_add        VARCHAR(255) NOT NULL,
    contract_date   DATE NOT NULL,
    sku             VARCHAR(12),
    PRIMARY KEY(tin),
    FOREIGN KEY(sku) REFERENCES product(sku),
    CHECK (sku > 7),
    CHECK (tin = '_________-__'),
);

CREATE TABLE employee(
    ssn         VARCHAR(11),    -- Based on USA's SSN, with the following layout XXX-XX-XXXX
    tin         INTEGER(9),     -- Based on Portugal's NIF, having only 9 digits
    bdate       DATE NOT NULL,
    emp_name    VARCHAR(80) NOT NULL,
    PRIMARY KEY(ssn),
    UNIQUE(tin),
    CHECK (tin = 9),
    CHECK (ssn = '___-__-____'),
    -- IC-3: Every emplyee must exist in the table 'works'
);

CREATE TABLE department(
    dep_name    VARCHAR(200),
    PRIMARY KEY(dep_name),
);

CREATE TABLE workplace(
    work_add    VARCHAR(255),
    lat         NUMERIC(8,6),
    long        NUMERIC(9,6),
    PRIMARY KEY(work_add),
    UNIQUE(lat,long),
);

CREATE TABLE office(
    work_add    VARCHAR(255),
    PRIMARY KEY(work_add),
    FOREIGN KEY(work_add) REFERENCES workplace(work_add),
);

CREATE TABLE warehouse(
    work_add    VARCHAR(255),
    PRIMARY KEY(work_add),
    FOREIGN KEY(work_add) REFERENCES workplace(work_add),
);

-- ASSOCIATIONS

CREATE TABLE pay (
    cust_no     INTEGER(10),
    order_no    INTEGER(12),
    PRIMARY KEY(order_no),
    FOREIGN KEY(cust_no) REFERENCES customer(cust_no),
    FOREIGN KEY(order_no) REFERENCES sale(order_no),
    CHECK (order_no > 0),
    CHECK (cust_no > 0),
);

CREATE TABLE has (
    --!! Contains cannot be used as a table name !!
    order_no    INTEGER(12),
    sku         VARCHAR(12),
    qty         INTEGER NOT NULL,
    PRIMARY KEY(order_no, sku),
    FOREIGN KEY(order_no) REFERENCES parcel(order_no),
    FOREIGN KEY(sku) REFERENCES product(sku),
    CHECK (sku > 7),
    CHECK (order_no > 0),
);

CREATE TABLE process (
    order_no    INTEGER(12),
    ssn         VARCHAR(11),
    PRIMARY KEY(order_no, ssn),
    FOREIGN KEY(order_no) REFERENCES parcel(order_no),
    FOREIGN KEY(ssn) REFERENCES employee(ssn),
    CHECK (ssn = '___-__-____'),
    CHECK (order_no > 0),
);

CREATE TABLE works (
    ssn         VARCHAR(11),
    dep_name    VARCHAR(200),
    work_add    VARCHAR(255),
    PRIMARY KEY(ssn, dep_name, work_addr),
    FOREIGN KEY(ssn) REFERENCES employee(ssn),
    FOREIGN KEY(dep_name) REFERENCES dep_name(department),
    FOREIGN KEY(work_add) REFERENCES work_add(workplace),
    CHECK (ssn = '___-__-____'),
);

CREATE TABLE delivery(
    work_add    VARCHAR(255),
    sku         VARCHAR(12),
    tin         VARCHAR(12),
    PRIMARY KEY(work_add, sku, tin),
    FOREIGN KEY(work_add) REFERENCES warehouse(work_add),
    FOREIGN KEY(sku, tin) REFERENCES supplier(sku, tin),
    CHECK (sku > 7),
    CHECK (tin > 8),
);