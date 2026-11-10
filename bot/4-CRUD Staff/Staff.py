class Staff:
    def __init__(
        self,
        staff_id=None,
        name=None,
        gender=None,
        position=None,
        department=None,
        salary=0.0,
        phone=None,
        email=None,
        is_active=True
    ):
        self._staff_id = staff_id
        self._name = name
        self._gender = gender
        self._position = position
        self._department = department
        self._salary = salary
        self._phone = phone
        self._email = email
        self._is_active = is_active

    # ==================== staff_id ====================
    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value

    # ==================== name ====================
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # ==================== gender ====================
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    # ==================== position ====================
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    # ==================== department ====================
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value

    # ==================== salary ====================
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = float(value) if value is not None else 0.0

    # ==================== phone ====================
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    # ==================== email ====================
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # ==================== is_active ====================
    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = bool(value)

    def __str__(self):
        status = "Active" if self._is_active else "Inactive"
        return (
            f"Staff(staff_id={self._staff_id}, name='{self._name}', gender='{self._gender}', "
            f"position='{self._position}', department='{self._department}', "
            f"salary={self._salary:.2f}, phone='{self._phone}', email='{self._email}', is_active={status})"
        )


# Alias for compatibility if needed
TBLStaff = Staff
