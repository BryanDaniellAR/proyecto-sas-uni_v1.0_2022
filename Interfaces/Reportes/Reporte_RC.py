# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bryan\Desktop\INICIO\QTDESIGNER\Reporte_RC.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from DataBase import Query
from datetime import datetime, timedelta
from Libreria.DetectorSemanas import *
from Libreria.ExportarTablaPDF import *
from Libreria.ExportarTablaExcel import *
from PyQt5 import QtCore, QtGui, QtWidgets,QtPrintSupport


class Ui_Form(object):
    def setupUi(self, Form,datos_obtenidos):
        global data_obtenida
        data_obtenida = datos_obtenidos

        Form.setObjectName("Form")
        Form.resize(1190, 668)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1191, 671))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(245, 0, 23, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnVolver = QtWidgets.QPushButton(Form)
        self.btnVolver.setGeometry(QtCore.QRect(930, 460, 201, 121))
        self.btnVolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVolver.setStyleSheet("QPushButton{\n"
        "color: rgb(48, 48, 48);\n"
        "font: 24pt \"Verdana\";\n"
        "border: 2px solid #FFB5B5;\n"
        "padding: 5px;\n"
        "border-radius: 3px;\n"
        "opacity: 200;\n"
        "cursor:pointer;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(243, 40, 40);\n"
        "}\n"
        "")
        self.btnVolver.setObjectName("btnVolver")
        self.tbAsistencia = QtWidgets.QTableWidget(Form)
        self.tbAsistencia.setGeometry(QtCore.QRect(110, 180, 781, 401))
        self.tbAsistencia.setStyleSheet("")
        self.tbAsistencia.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbAsistencia.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbAsistencia.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbAsistencia.setObjectName("tbAsistencia")
        self.tbAsistencia.setColumnCount(3)
        self.tbAsistencia.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbAsistencia.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAsistencia.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbAsistencia.setHorizontalHeaderItem(2, item)
        self.tbAsistencia.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        global qtabla
        qtabla = self.tbAsistencia

        self.btnAbrirRE = QtWidgets.QPushButton(Form)
        self.btnAbrirRE.setGeometry(QtCore.QRect(230, 610, 241, 31))
        self.btnAbrirRE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAbrirRE.setStyleSheet("QPushButton{\n"
        "color: rgb(48, 48, 48);\n"
        "font: 12pt \"Verdana\";\n"
        "border: 2px solid #FFB5B5;\n"
        "padding: 5px;\n"
        "border-radius: 3px;\n"
        "opacity: 200;\n"
        "cursor:pointer;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(243, 40, 40);\n"
        "}\n"
        "")
        self.btnAbrirRE.setObjectName("btnAbrirRE")
        self.label_42 = QtWidgets.QLabel(Form)
        self.label_42.setGeometry(QtCore.QRect(30, 20, 911, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.btnImprimir = QtWidgets.QPushButton(Form)
        self.btnImprimir.setGeometry(QtCore.QRect(510, 610, 241, 31))
        self.btnImprimir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnImprimir.setStyleSheet("QPushButton{\n"
        "color: rgb(48, 48, 48);\n"
        "font: 12pt \"Verdana\";\n"
        "border: 2px solid #FFB5B5;\n"
        "padding: 5px;\n"
        "border-radius: 3px;\n"
        "opacity: 200;\n"
        "cursor:pointer;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(243, 40, 40);\n"
        "}\n"
        "")
        self.btnImprimir.setObjectName("btnImprimir")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cbPeriodo = QtWidgets.QComboBox(Form)
        self.cbPeriodo.setGeometry(QtCore.QRect(110, 130, 131, 22))
        self.cbPeriodo.setObjectName("cbPeriodo")

        global ComboPeriodo
        ComboPeriodo = self.cbPeriodo

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbClase = QtWidgets.QLabel(Form)
        self.lbClase.setGeometry(QtCore.QRect(110, 80, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        self.lbClase.setFont(font)
        self.lbClase.setObjectName("lbClase")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        fecha_actual = format(datetime.today().year)+"-"+format(datetime.today().month)+"-"+format(datetime.today().day)

        #INGRESAREMOS EL VALOR DE LA CLASE SELECCIONADA
        #------------------------------------------------
        self.lbClase.setText(datos_obtenidos[2])# ╝@@╝
        #OBTENDREMOS LA LISTA DE PERIODO LLENADO POR PRIMERA VEZ
        #------------------------------------------------
        lista_periodo = Query.informacion_periodo()
        descripcion_periodo = []
        for i in lista_periodo:
            descripcion_periodo.append(i[1])
        self.cbPeriodo.addItems(descripcion_periodo) #╝@@╝
        #------------------------------------------------------
        #OBTENDREMOS LA CANTIDAD DE SEMANAS QUE HAY
        #--------------------------------------------------------
        lista_semana = deteccion_semanas(lista_periodo[0][2],lista_periodo[0][3],'%Y-%m-%d')

        global semana_inicial

        semana_inicial = []
        for i in range(lista_semana):
            semana_inicial.append("Semana "+str(i+1)) #╝@@╝    
        #--------------------------------------------------------
        #OBTENDREMOS LA LISTA DE DIAS DE ESTA CLASE
        #--------------------------------------------------------
        lista_dias_semana = Query.dias_clase(data_obtenida[2])

        global dias_semana_inicial

        dias_semana_inicial = []
        for i in lista_dias_semana:
            dias_semana_inicial.append(i[1]) #╝@@╝
        #--------------------------------------------------------
        #INGRESAREMOS EL VALOR DEL PERIODO ACTUAL Y SEMANA ACTUAL
        datos_semana_actual = identificarSemanaActual(lista_periodo,fecha_actual)

        #--------------------------------------------------------
        #LLENADO DE TABLA PRIMERA VEZ # ---------------**-*-*-*-*-*-*-*
        #self.tbAsistencia.setRowCount(len(semana_inicial))
        dias = len(dias_semana_inicial)
        #self.tbAsistencia.setColumnCount(dias*2+1)
        #_translate = QtCore.QCoreApplication.translate
        #self.tbAsistencia.setColumnCount(dias*2)
        #contador = 0

        alumnos_matriculados_curso = Query.alumnos_clase_periodo(datos_obtenidos[2],self.cbPeriodo.currentText())
        alumnos_de_reporte_as_asistencia = SepararListaAlumnosReporteRC(alumnos_matriculados_curso)
        
        self.tbAsistencia.setRowCount(len(alumnos_de_reporte_as_asistencia))
        for a in range(len(alumnos_de_reporte_as_asistencia)):
            for b in range(len(alumnos_de_reporte_as_asistencia[0])):
                self.tbAsistencia.setItem(a,b, QtWidgets.QTableWidgetItem(alumnos_de_reporte_as_asistencia[a][b]))
        self.tbAsistencia.resizeColumnsToContents()

        #----------------------------------
        #AL SELECCIONAR UN COMBO BOX
        self.cbPeriodo.currentTextChanged.connect(self.PresionarPeriodo) #╝@@╝
        #print(self.cbSemana.currentText())
        #if(self.cbSemana.currentIndex() !=0):
        global valor_dejado_periodo
        valor_dejado_periodo = []
        valor_dejado_periodo.append(self.cbPeriodo.currentText())
        #-----------------------------
        #AL DAR CLICK EN LA BUSQUEDA
        global tabla_inicial
        tabla_inicial = []
        #self.etBuscar.textChanged.connect(self.BuscarTabla)
        #Dar CLICK EN IMPRIMIR
        #------------------------------------
        self.btnImprimir.clicked.connect(self.ImprimirTabla)
        #------------------------------------
        #Dar CLICK EN BOTON PARA EXCEL
        #------------------------------------
        self.btnAbrirRE.clicked.connect(self.ExportarExcel)
        #------------------------------------
        #DAR CLICK EN VOLVER
        self.btnVolver.clicked.connect(Form.close)
        #------------------------------

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnVolver.setText(_translate("Form", "VOLVER"))
        item = self.tbAsistencia.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Código"))
        item = self.tbAsistencia.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Alumno"))
        item = self.tbAsistencia.horizontalHeaderItem(2)
        item.setText(_translate("Form", "N° de Asistencias"))
        self.btnAbrirRE.setText(_translate("Form", "ABRIR REPORTE EN EXCEL"))
        self.label_42.setText(_translate("Form", "REPORTE DE ASISTENCIA EN EL CICLO"))
        self.btnImprimir.setText(_translate("Form", "IMPRIMIR"))
        self.label_7.setText(_translate("Form", "Periodo:"))
        self.label_3.setText(_translate("Form", "Clase:"))
        self.lbClase.setText(_translate("Form", "Seleccione una clase"))

    def PresionarPeriodo(self,Form):
        self.tbAsistencia.clearContents()
        alumnos_matriculados_curso = Query.alumnos_clase_periodo(data_obtenida[2],self.cbPeriodo.currentText())
        alumnos_de_reporte_as_asistencia = SepararListaAlumnosReporteRC(alumnos_matriculados_curso)
        self.tbAsistencia.setRowCount(len(alumnos_de_reporte_as_asistencia))
        for a in range(len(alumnos_de_reporte_as_asistencia)):
            for b in range(len(alumnos_de_reporte_as_asistencia[0])):
                self.tbAsistencia.setItem(a,b, QtWidgets.QTableWidgetItem(alumnos_de_reporte_as_asistencia[a][b]))
        self.tbAsistencia.resizeColumnsToContents()

    def ImprimirTabla(self,Form):
        exportarPDF(self.tbAsistencia,"ReporteRS.("+ComboPeriodo.currentText()+")")
    
    def ExportarExcel(self,Form):
        cabezera = cabezeraActualTabla()
        lista_tabla_actual = listaActualTabla()
        exportarExcel(lista_tabla_actual,cabezera,"ReporteRS.("+ComboPeriodo.currentText()+")")

def identificarSemanaActual(lista_periodo,fecha_actual):
    datos_semana = []
    for i in lista_periodo:
        if(fecha_actual>=i[2] and fecha_actual<= i[3]):
            semana_actual = deteccion_semanas(i[2],fecha_actual,'%Y-%m-%d')
            #semana_actual = int((fecha_actual-i[2])/7)
            datos_semana.append(i[1])
            datos_semana.append(str(semana_actual+1))
            return datos_semana
    return datos_semana

def SepararListaAlumnosReporteRC(lista_alumnos):
    alumnos_de_reporte_rc = []
    alumnos_clase_periodo = lista_alumnos
    #semana_numero_int = [int(temp)for temp in qsemana.currentText().split() if temp.isdigit()]
    if len(alumnos_clase_periodo)>0:
        for a in range(len(alumnos_clase_periodo)):
            lista_separada=[]
            lista_separada.append(alumnos_clase_periodo[a][0])
            lista_separada.append(alumnos_clase_periodo[a][1])
            cantidad_asistencia_en_curso = Query.acumulado_asistencia_alumno(data_obtenida[2],ComboPeriodo.currentText(),alumnos_clase_periodo[a][0])
            lista_separada.append(str(cantidad_asistencia_en_curso[0][0]))
            alumnos_de_reporte_rc.append(lista_separada)
    return alumnos_de_reporte_rc

def listaActualTabla():
    rows = qtabla.rowCount()
    for n in range(rows):
        fila=[]
        for column in range(qtabla.model().columnCount()):
            fila.append(qtabla.item(n, column).text())
        tabla_inicial.append(fila)
    return tabla_inicial

def cabezeraActualTabla():
    cabezera_obtenido = []
    for i in range(qtabla.model().columnCount()):
        label = qtabla.horizontalHeaderItem(i).text()
        cabezera_obtenido.append(label)
    return cabezera_obtenido
