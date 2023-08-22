from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # defining labels, input boxes and button
        self.output_label = QLabel("")   
        self.button = QPushButton("Calculate") 
        time_label = QLabel("Time (hours)")
        self.time_input_box = QLineEdit()  

        # adding combo box for km/miles
        combo = QComboBox()
        combo.addItems(['Metric (km)', 'Imperial (mi)'])

        if combo.currentText() == 'Metric (km)':
            distance_label = QLabel("Distance")
            self.distance_input_box = QLineEdit()
            self.button.clicked.connect(self.calculate_km)
            
        if combo.currentText() == 'Imperial (mi)':
            distance_label = QLabel("Distance")
            self.distance_input_box = QLineEdit()
        
        # adding widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input_box, 0, 1)
        grid.addWidget(combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input_box, 1, 1)
        grid.addWidget(self.button, 2, 0, 1, 3)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)
    
    def calculate_km(self):
        speed = float(self.distance_input_box.text()) / float(self.time_input_box.text())

        self.output_label.setText(f"Average speed: {speed} km/h")

    def calculate_mi(self):
        speed = float(self.distance_input_box.text()) / float(self.time_input_box.text())

        self.output_label.setText(f"Average speed: {speed} mi/h")



app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())

        