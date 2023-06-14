insert into customer 
values  (1,'Manuel Pereira',     'manuel345@hotmail.com','983838383','Av. Eng. Adelino Amaro da Costa,485,2750-642,Cascais'), -- [Street],[Number],[Postal code],[City]
        (2,'Josefina Silva',     'jsilva.pt@gmail.com',  '916990129','Casal da Torre,4,2775-405,Carcavelos'),
        (3,'Daniela Belchior',   'danibel98@hotmail.com','982942069','R. Actriz Adelina Fernandes,21B,2795-092,Linda-a-Velha'),
        (4,'Francisco Rodrigues','kikorod@sapo.pt',      '952637194','R. Prof. Xavier Morato,8,1600-598,Lisboa'),
        (5,'Miguel Seleiro',     'mseleiro@gmail.com',   '965783162','R. Dom Afonso Henriques,49,2695-691,São João da Talha');

START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED; -- Because of IC 3
insert into orders
values  (1,1,'2019-01-01'), -- paid
        (2,2,'2022-02-13'),
        (3,3,'2022-04-09'), -- paid
        (4,1,'2023-05-27'), -- paid
        (5,5,'2022-11-25'), -- paid
        (6,3,'2023-12-12'),
        (7,4,'2021-12-30'), -- paid
        (8,5,'2020-01-27'); -- paid

insert into product
values  ('BAN-12345','Banana',                'Bananas from Madeira 1kg',                     2.82,  738913481),
        ('SAL-67890','Salt',                  'Thin salt 1kg',                                2.18,  NULL),
        ('BW-13579', 'Body Gel',              'Dove Body Gel with orange scent 750ml',        6.49,  NULL),
        ('RIC-24680','White Rice',            'Auchan white rice 250g',                       1.49,  9394859123),
        ('OIL-86420','Extra Virgin Olive Oil','Alentejo Natural extra virgin olive oil 750ml',5.93,  NULL),
        ('VOD-34932','Vodka',                 'Pure vodka from Russia',                       50.49, NULL),
        ('WAB-12312','Wagyu Beef',            'Premium gourmet japanese beef',                126.85,1279312789);

insert into contains
values  (1, 'OIL-86420', 4),
        (2, 'RIC-24680', 16),
        (3, 'BW-13579',  7),
        (3, 'RIC-24680', 1),
        (4, 'SAL-67890', 9),
        (5, 'RIC-24680', 12),
        (6, 'BAN-12345', 20),
        (7, 'VOD-34932', 4),
        (8, 'WAB-12312', 1);
COMMIT;

insert into supplier
values  ('12839471-ST','Salty Time',     'Rua dos Alecrins',   'SAL-67890','2019-05-07'),
        ('14958313-DL','Deloitte',       'Rua dos Alecrins',   'RIC-24680','2020-06-13'),
        ('14937593-ON','Oilly Needs',    'Rua do Paraiso',     'OIL-86420','2021-10-27'),
        ('15631098-IB','InBath',         'Rua dos Setes Ceus', 'BW-13579', '2019-10-05'),
        ('10123943-MP','Monkey Paradise','Travessa da Amorosa','BAN-12345','2021-01-18'),
        ('49328701-RS','Ruski',          'Praça da Russia'    ,'VOD-34932','2022-07-17'),
        ('12334535-OP','OnlyPremium',    'Avenida Duarte Pach','WAB-12312','2018-04-01');

insert into employee 
values  ('222-32-4534',823791271,'1990-08-23','Joao Maria Augusto'),
        ('398-25-9710',279301898,'2000-03-09','Maria Jose Gonçalves'),
        ('947-83-7469',238523471,'1994-06-03','Albertino Rocha'),
        ('340-29-4301',134587398,'1992-03-05','Francisca Pires');

insert into department
values  ('Human Resources'),
        ('Customer Support'),
        ('Product Management');

START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED; -- Because of IC 2
insert into workplace
values  ('R. Rui Teles Palhinha,6,2740-278,Porto Salvo',25.6,893.90),
        ('Pátio do Tijolo,11,1200-230,Lisboa',          49.6,700.34),
        ('Alto do Varejão,10A,1900-433,Lisboa',         89.32,13.87),
        ('R. Rui Teles Palhinha,8,2740-278,Porto Salvo',26.0,893.90),
        ('R. de Pedro Hispano,880,4250-364,Porto',      60.7,324.4);

insert into office
values  ('R. Rui Teles Palhinha,6,2740-278,Porto Salvo'),
        ('R. Rui Teles Palhinha,8,2740-278,Porto Salvo');

insert into warehouse
values  ('Pátio do Tijolo,11,1200-230,Lisboa'),
        ('Alto do Varejão,10A,1900-433,Lisboa'),
        ('R. de Pedro Hispano,880,4250-364,Porto');
COMMIT;

insert into pay
values  (1,1),
        (3,3),
        (4,1),
        (5,5),
        (7,4),
        (8,5);

insert into process
values  ('947-83-7469',1),
        ('222-32-4534',2),
        ('340-29-4301',8);

insert into works
values  ('398-25-9710','Human Resources',   'R. Rui Teles Palhinha,6,2740-278,Porto Salvo'),
        ('222-32-4534','Customer Support',  'R. Rui Teles Palhinha,8,2740-278,Porto Salvo'),
        ('947-83-7469','Human Resources',   'Alto do Varejão,10A,1900-433,Lisboa'),
        ('340-29-4301','Product Management','R. de Pedro Hispano,880,4250-364,Porto');

insert into delivery
values  ('R. de Pedro Hispano,880,4250-364,Porto','12839471-ST'),
        ('Pátio do Tijolo,11,1200-230,Lisboa',    '10123943-MP'),
        ('Alto do Varejão,10A,1900-433,Lisboa',   '14958313-DL'),
        ('Alto do Varejão,10A,1900-433,Lisboa',   '14937593-ON'),
        ('Pátio do Tijolo,11,1200-230,Lisboa',    '15631098-IB'),
        ('R. de Pedro Hispano,880,4250-364,Porto','49328701-RS'),
        ('R. de Pedro Hispano,880,4250-364,Porto','12334535-OP');