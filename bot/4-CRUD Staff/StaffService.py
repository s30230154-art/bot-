from connection import Connection
from Staff import Staff


class StaffService(Connection):

    def get_staff_by_id(self, staff_id: int):
        conn = self._get_connection()
        if not conn:
            return None
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT staff_id, name, gender, position, department, salary, phone, email, is_active 
                    FROM tbl_staff 
                    WHERE staff_id = %s;
                    """,
                    (staff_id,)
                )
                row = cursor.fetchone()
                if row:
                    return Staff(
                        staff_id=row[0],
                        name=row[1],
                        gender=row[2],
                        position=row[3],
                        department=row[4],
                        salary=float(row[5]) if row[5] is not None else 0.0,
                        phone=row[6],
                        email=row[7],
                        is_active=row[8]
                    )
                return None
        except Exception as ex:
            print(f"Error fetching staff: {ex}")
            return None
        finally:
            conn.close()

    def insert_staff(self, new_staff: Staff) -> bool:
        conn = self._get_connection()
        if not conn:
            return False
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO tbl_staff (name, gender, position, department, salary, phone, email, is_active)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING staff_id;
                    """,
                    (
                        new_staff.name,
                        new_staff.gender,
                        new_staff.position,
                        new_staff.department,
                        new_staff.salary,
                        new_staff.phone,
                        new_staff.email,
                        new_staff.is_active
                    )
                )
                new_staff.staff_id = cursor.fetchone()[0]
                conn.commit()
                return True
        except Exception as ex:
            print(f"Error adding staff: {ex}")
            conn.rollback()
            return False
        finally:
            conn.close()

    # Alias for insert_staff
    add_staff = insert_staff

    def update_staff(self, staff: Staff) -> bool:
        conn = self._get_connection()
        if not conn:
            return False
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE tbl_staff 
                    SET name = %s, gender = %s, position = %s, department = %s, 
                        salary = %s, phone = %s, email = %s, is_active = %s
                    WHERE staff_id = %s
                    RETURNING staff_id;
                    """,
                    (
                        staff.name,
                        staff.gender,
                        staff.position,
                        staff.department,
                        staff.salary,
                        staff.phone,
                        staff.email,
                        staff.is_active,
                        staff.staff_id
                    )
                )
                result = cursor.fetchone()
                if result:
                    conn.commit()
                    return True
                return False
        except Exception as ex:
            print(f"Error updating staff: {ex}")
            conn.rollback()
            return False
        finally:
            conn.close()

    def delete_staff(self, staff_id: int) -> bool:
        conn = self._get_connection()
        if not conn:
            return False
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM tbl_staff WHERE staff_id = %s;", (staff_id,))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as ex:
            print(f"Error deleting staff: {ex}")
            conn.rollback()
            return False
        finally:
            conn.close()

    # Alias for delete_staff
    delete_staff_by_id = delete_staff

    def get_all_staff(self) -> list:
        conn = self._get_connection()
        if not conn:
            return []
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT staff_id, name, gender, position, department, salary, phone, email, is_active 
                    FROM tbl_staff 
                    ORDER BY staff_id ASC;
                    """
                )
                rows = cursor.fetchall()
                staff_list = [
                    Staff(
                        staff_id=row[0],
                        name=row[1],
                        gender=row[2],
                        position=row[3],
                        department=row[4],
                        salary=float(row[5]) if row[5] is not None else 0.0,
                        phone=row[6],
                        email=row[7],
                        is_active=row[8]
                    )
                    for row in rows
                ]
                return staff_list
        except Exception as ex:
            print(f"Error fetching staff list: {ex}")
            return []
        finally:
            conn.close()

    # Alias for get_all_staff
    get_all_staffs = get_all_staff

    def menu_staff(self):
        while True:
            print("\n=== Manage Staff System ===")
            print("1. Get staff by id")
            print("2. Get all staff")
            print("3. Insert staff")
            print("4. Update staff")
            print("5. Delete staff")
            print("6. Exit menu")
            try:
                option = int(input("Enter your option: "))
            except ValueError:
                print("Invalid option. Please enter a number.")
                continue

            if option == 1:
                print("======= Get Staff by ID ======")
                try:
                    s_id = int(input("Please enter staff id: "))
                    staff = self.get_staff_by_id(s_id)
                    if staff is None:
                        print(f"Staff ID: {s_id} not found.")
                    else:
                        print(staff)
                except ValueError:
                    print("Invalid ID format.")

            elif option == 2:
                print("======= All Staff ======")
                staffs = self.get_all_staff()
                if not staffs:
                    print("No staff found.")
                else:
                    for s in staffs:
                        print(s)

            elif option == 3:
                print("======= Add Staff ======")
                name = input("Please enter name: ").strip()
                gender = input("Please enter gender (Male/Female): ").strip()
                position = input("Please enter position: ").strip()
                department = input("Please enter department: ").strip()
                try:
                    salary = float(input("Please enter salary: ").strip() or "0")
                except ValueError:
                    salary = 0.0
                phone = input("Please enter phone: ").strip()
                email = input("Please enter email: ").strip()
                is_active_input = input("Is active? (y/n, default y): ").strip().lower()
                is_active = False if is_active_input == 'n' else True

                new_staff = Staff(
                    name=name,
                    gender=gender,
                    position=position,
                    department=department,
                    salary=salary,
                    phone=phone,
                    email=email,
                    is_active=is_active
                )
                if self.insert_staff(new_staff):
                    print(f"Added staff successfully with ID: {new_staff.staff_id}")
                else:
                    print("Failed to add staff.")

            elif option == 4:
                print("======= Update Staff ======")
                try:
                    s_id = int(input("Please enter staff id: "))
                    staff = self.get_staff_by_id(s_id)
                    if staff is None:
                        print(f"Staff ID: {s_id} not found.")
                    else:
                        name = input(f"Please enter name [{staff.name}]: ").strip()
                        if name != "":
                            staff.name = name

                        gender = input(f"Please enter gender [{staff.gender}]: ").strip()
                        if gender != "":
                            staff.gender = gender

                        position = input(f"Please enter position [{staff.position}]: ").strip()
                        if position != "":
                            staff.position = position

                        department = input(f"Please enter department [{staff.department}]: ").strip()
                        if department != "":
                            staff.department = department

                        salary_str = input(f"Please enter salary [{staff.salary}]: ").strip()
                        if salary_str != "":
                            try:
                                staff.salary = float(salary_str)
                            except ValueError:
                                print("Invalid salary format, kept existing value.")

                        phone = input(f"Please enter phone [{staff.phone}]: ").strip()
                        if phone != "":
                            staff.phone = phone

                        email = input(f"Please enter email [{staff.email}]: ").strip()
                        if email != "":
                            staff.email = email

                        active_str = input(f"Is active? (y/n) [{staff.is_active}]: ").strip().lower()
                        if active_str == 'y':
                            staff.is_active = True
                        elif active_str == 'n':
                            staff.is_active = False

                        if self.update_staff(staff):
                            print("Updated staff successfully.")
                        else:
                            print("Update staff failed.")
                except ValueError:
                    print("Invalid ID format.")

            elif option == 5:
                print("======= Delete Staff ======")
                try:
                    s_id = int(input("Please enter staff id to delete: "))
                    if self.delete_staff(s_id):
                        print(f"Deleted staff ID: {s_id} successfully.")
                    else:
                        print(f"Failed to delete staff ID: {s_id} or ID does not exist.")
                except ValueError:
                    print("Invalid ID format.")

            elif option == 6:
                print("Exiting menu. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 6.")

    # Alias for menu
    menu = menu_staff


def menu_staff():
    """Standalone function to run staff menu."""
    service = StaffService()
    service.menu_staff()


if __name__ == "__main__":
    menu_staff()
