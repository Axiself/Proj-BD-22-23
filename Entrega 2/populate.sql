insert into customer values (DEFAULT,'Manuel Pereira',     'manuel345@hotmail.com','983838383','Rua das Galinhas');
insert into customer values (DEFAULT,'Josefina Silva',     'jsilva.pt@gmail.com',  '916990129','Rua das Caldeiras');
insert into customer values (DEFAULT,'Daniela Belchior',   'danibel98@hotmail.com','982942069','Avenida das Borboletas');
insert into customer values (DEFAULT,'Francisco Rodrigues','kikorod@sapo.pt',      '952637194','Rua do Monte de Cima');
insert into customer values (DEFAULT,'Miguel Seleiro',     'mseleiro@gmail.com',   '965783162','Estrada do Supermitra');

insert into parcel values (DEFAULT,'2023-01-01',1);
insert into parcel values (DEFAULT,'2023-02-13',2);
insert into parcel values (DEFAULT,'2023-04-09',3);
insert into parcel values (DEFAULT,'2023-05-27',1);
insert into parcel values (DEFAULT,'2023-11-25',5);
insert into parcel values (DEFAULT,'2023-12-12',3);
insert into parcel values (DEFAULT,'2023-12-30',4);

insert into sale values (1);
insert into sale values (3);
insert into sale values (4);
insert into sale values (5);
insert into sale values (7);

insert into product values('BAN-12345','Banana',                'Bananas from Madeira 1kg',                     2.82);
insert into product values('SAL-67890','Salt',                  'Thin salt 1kg',                                2.18);
insert into product values('BW-13579', 'Body Gel',              'Dove Body Gel with orange scent 750ml',        6.49);
insert into product values('RIC-24680','White Rice',            'Auchan white rice 250g',                       1.49);
insert into product values('OIL-86420','Extra Virgin Olive Oil','Alentejo Natural extra virgin olive oil 750ml',5.93);

insert into eanproduct values('BAN-12345','GS17389134814');
insert into eanproduct values('RIC-24680','GS19394859123');

insert into supplier values('12839471-ST','Salty Time',     'Rua dos Alecrins',   '2019-05-07','SAL-67890');
insert into supplier values('14958313-DL','Deloitte',       'Rua dos Alecrins',   '2020-06-13','RIC-24680');
insert into supplier values('14937593-ON','Oilly Needs',    'Rua do Paraiso',     '2021-10-27','OIL-86420');
insert into supplier values('15631098-IB','InBath',         'Rua dos Setes Ceus', '2019-10-05','BW-13579');
insert into supplier values('10123943-MP','Monkey Paradise','Travessa da Amorosa','2021-01-18','BAN-12345');

insert into employee values('222-32-4534',823791271,'1990-08-23','Joao Maria');
insert into employee values('398-25-9710',279301898,'2000-03-09','Maria Jose');
insert into employee values('947-83-7469',238523471,'1994-06-03','Albertino Rocha');

insert into department values('Human Resources');
insert into department values('Customer Support');

insert into workplace values('Rua do Sol',           25.6,893.90);
insert into workplace values('Avenida das flores',   49.6,700.34);
insert into workplace values('Rua dos Sonhos',       89.32,13.87);
insert into workplace values('Avenida das Oliveiras',15.6,80.1);

insert into office values('Rua do Sol');
insert into office values('Avenida das Oliveiras');

insert into warehouse values('Rua do Sol');
insert into warehouse values('Avenida das flores');
insert into warehouse values('Rua dos Sonhos');

insert into pay values(1,1);
insert into pay values(3,3);
insert into pay values(1,4);
insert into pay values(5,5);
insert into pay values(4,7);

insert into has values(1, 'OIL-86420', 4);
insert into has values(2, 'RIC-24680', 16);
insert into has values(3, 'BW-13579',  7);
insert into has values(3, 'RIC-24680', 1);
insert into has values(4, 'SAL-67890', 9);
insert into has values(5, 'RIC-24680', 12);
insert into has values(6, 'BAN-12345', 20);
insert into has values(7, 'OIL-86420', 4);

insert into process values(2,'222-32-4534');
insert into process values(1,'947-83-7469');

insert into works values('398-25-9710','Human Resources','Rua do Sol');
insert into works values('222-32-4534','Customer Support','Avenida das Oliveiras');
insert into works values('947-83-7469','Human Resources','Rua dos Sonhos');

insert into delivery values('Rua do Sol',        'SAL-67890','12839471-ST');
insert into delivery values('Avenida das flores','BAN-12345','10123943-MP');
insert into delivery values('Rua do Sol',        'RIC-24680','14958313-DL');
insert into delivery values('Rua dos Sonhos',    'OIL-86420','14937593-ON');
insert into delivery values('Avenida das flores','BW-13579', '15631098-IB');