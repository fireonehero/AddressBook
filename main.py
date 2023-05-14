import sys
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QSizePolicy, QTextEdit, QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget, QLineEdit
from PyQt5.QtCore import Qt

contactList = {}

class MainWindow(QWidget):
    def __init__(self, view_all, parent = None):
        super(MainWindow, self).__init__(parent)

        # Add a new contact button
        self.addC_button = QPushButton("Add new contact.")
        self.addC_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.addC_button.clicked.connect(self.switchScreenAdd)

        # Remove a contact button
        self.removeC_button = QPushButton("Remove a contact.")
        self.removeC_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.removeC_button.clicked.connect(self.switchScreenRemove)

        # Edit a contact button
        self.editC_button = QPushButton("Edit a contact.")
        self.editC_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.editC_button.clicked.connect(self.switchScreenEdit)

        # View all contacts button
        self.viewC_button = QPushButton("View all contacts.")
        self.viewC_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.viewC_button.clicked.connect(self.switchScreenViewA)

        # Store the view_all widget
        self.view_all = view_all  

        # Layout Management
        layout = QVBoxLayout()
        layout.addWidget(self.addC_button)
        layout.addWidget(self.removeC_button)
        layout.addWidget(self.editC_button)
        layout.addWidget(self.viewC_button)
        self.setLayout(layout)

    def switchScreenAdd(self):
        main_widget.setCurrentIndex(1)

    def switchScreenRemove(self):
        main_widget.setCurrentIndex(2)

    def switchScreenEdit(self):
        main_widget.setCurrentIndex(3)

    def switchScreenViewA(self):
        self.view_all.displayContacts()
        main_widget.setCurrentIndex(4)


class AddPerson(QWidget):
    def __init__(self, parent=None):
        super(AddPerson, self).__init__(parent)
        # Name Box
        self.name_box = QLineEdit()
        self.name_box.setPlaceholderText("Name")

        # Phone Box
        self.phone_box = QLineEdit()
        self.phone_box.setPlaceholderText("Phone")

        # Email Box
        self.email_box = QLineEdit()
        self.email_box.setPlaceholderText("Email")

        # Address Box
        self.address_box = QLineEdit()
        self.address_box.setPlaceholderText("Address")

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.addContact)

        # Back Button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.switchScreen)

        # Layout management
        layout = QVBoxLayout()
        layout.addWidget(self.name_box)
        layout.addWidget(self.phone_box)
        layout.addWidget(self.email_box)
        layout.addWidget(self.address_box)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def addContact(self):
        global contactList
        name = self.name_box.text()
        phone = self.phone_box.text()
        email = self.email_box.text()
        address = self.address_box.text()
        contactList[name] = phone, email, address
        self.switchScreen()

    def switchScreen(self):
        self.name_box.clear()
        self.phone_box.clear()
        self.email_box.clear()
        self.address_box.clear()
        main_widget.setCurrentIndex(0)

class RemovePerson(QWidget):
    def __init__(self, parent = None):
        super(RemovePerson, self).__init__(parent)
        # Starting the name text box
        self.name_box = QLineEdit()
        self.name_box.setPlaceholderText("Enter contact name to remove")
        
        # Added the remove button
        self.remove_button = QPushButton("Remove")
        self.remove_button.clicked.connect(self.removeContact)
        
        # Back Button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.switchScreen)
        
        # Layout management
        layout = QVBoxLayout()
        layout.addWidget(self.name_box)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
        
    def removeContact(self):
        # Calling the global dictionary
        global contactList
        # Starting the name text box
        name = self.name_box.text()
        # If the name they enter is in the dictionary, it removes it
        if name in contactList:
            del contactList[name]
            print(f"{name} removed. Updated contact list: {contactList}")
        else:
            print(f"{name} not found in contact list.")
        self.switchScreen()

    def switchScreen(self):
        self.name_box.clear()
        main_widget.setCurrentIndex(0)

class EditContact(QWidget):
    def __init__(self, parent = None):
        super(EditContact, self).__init__(parent)
        # Name Box
        self.name_box = QLineEdit()
        self.name_box.setPlaceholderText("Enter contact name to change.")
        
        # Phone Box
        self.phone_box = QLineEdit()
        self.phone_box.setPlaceholderText("Enter new phone number.")
        
        # Email Box
        self.email_box = QLineEdit()
        self.email_box.setPlaceholderText("Enter new email.")
        
        # Address Box
        self.address_box = QLineEdit()
        self.address_box.setPlaceholderText("Enter new address.")
        
        # Change Button
        self.change_button = QPushButton("Change")
        self.change_button.clicked.connect(self.EditPerson)
        
        # Back Button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.switchScreen)
        
        # Layout Management
        layout = QVBoxLayout()
        layout.addWidget(self.name_box)
        layout.addWidget(self.phone_box)
        layout.addWidget(self.email_box)
        layout.addWidget(self.address_box)
        layout.addWidget(self.change_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)

    def EditPerson(self):
        global contactList
        name = self.name_box.text()
        phone = self.phone_box.text()
        email = self.email_box.text()
        address = self.address_box.text()
        if name in contactList:
            contactList[name] = phone, email, address
        self.switchScreen()

    def switchScreen(self):
        self.name_box.clear()
        self.phone_box.clear()
        self.email_box.clear()
        self.address_box.clear()
        main_widget.setCurrentIndex(0)
        
class ViewAll(QWidget):
    def __init__(self, parent = None):
        super(ViewAll, self).__init__(parent)
        self.table_widget = QTableWidget(0, 4)  # 0 rows, 4 columns
        self.table_widget.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Address"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.return_button = QPushButton("Return")
        self.return_button.clicked.connect(self.switchScreen)
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.return_button)
        self.setLayout(layout)

    def displayContacts(self):
        global contactList
        self.table_widget.setRowCount(len(contactList))  # Set the number of rows in the table
        for i, (name, details) in enumerate(contactList.items()):
            self.table_widget.setItem(i, 0, QTableWidgetItem(name))
            self.table_widget.setItem(i, 1, QTableWidgetItem(details[0]))  # Phone
            self.table_widget.setItem(i, 2, QTableWidgetItem(details[1]))  # Email
            self.table_widget.setItem(i, 3, QTableWidgetItem(details[2]))  # Address

    def switchScreen(self):
        self.table_widget.clearContents()  # Clear the table contents
        self.table_widget.setRowCount(0)  # Reset the number of rows in the table
        main_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    main_widget = QStackedWidget()

    view_all_widget = ViewAll()
    main_widget.addWidget(MainWindow(view_all_widget))
    main_widget.addWidget(AddPerson())
    main_widget.addWidget(RemovePerson())
    main_widget.addWidget(EditContact())
    main_widget.addWidget(view_all_widget)
    
    main_widget.show()
    app.exec_()
