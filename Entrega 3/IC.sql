DROP TRIGGER IF EXISTS check_mandatory_exclusive_workplace_specialisation ON workplace CASCADE;
DROP TRIGGER IF EXISTS check_mandatory_order_participation ON orders CASCADE;

ALTER TABLE employee
ADD CONSTRAINT underage_employee_check
CHECK (
    (CURRENT_DATE - employee.bdate) >= (365 * 18)
);


CREATE OR REPLACE FUNCTION check_mandatory_exclusive_workplace_specialisation()
	RETURNS TRIGGER AS
$$
    BEGIN
	    IF NEW.address NOT IN (SELECT address FROM office) AND NEW.address NOT IN (SELECT address FROM warehouse) THEN
		    RAISE EXCEPTION 'Workplace "%" must be either an office or a warehouse', NEW.address;
        END IF;

        IF NEW.address IN (SELECT address FROM office) AND NEW.address IN (SELECT address FROM warehouse) THEN
            RAISE EXCEPTION 'Workplace "%" cannot be both an office and a warehouse', NEW.address;
        END IF;
	    RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER mandatory_workplace_exclusive_specialisation
AFTER INSERT OR UPDATE ON workplace DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE check_mandatory_exclusive_workplace_specialisation();


CREATE OR REPLACE FUNCTION check_mandatory_order_participation()
    RETURNS TRIGGER AS
$$
    BEGIN
        IF NEW.order_no NOT IN (SELECT order_no FROM contains) OR NEW.order_no IN (SELECT order_no FROM contains WHERE contains.qty = 0 ) THEN
            RAISE EXCEPTION 'Order "%" must contain at least one product', NEW.order_no;
        END IF;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE CONSTRAINT TRIGGER mandatory_order_participation 
AFTER INSERT OR UPDATE ON orders DEFERRABLE
FOR EACH ROW EXECUTE PROCEDURE check_mandatory_order_participation();