import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from ext import *

class Main(QtGui.QMainWindow):

        def __init__(self, parent = None):
                QtGui.QMainWindow.__init__(self,parent)

                self.filename = ""
                self.initUI()
                self.changesSaved = True

        def initToolbar(self):
                self.newAction  = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
                self.newAction.setStatusTip("Create a new document from scratch.")
                self.newAction.setShortcut("Ctrl+N")
                self.newAction.triggered.connect(self.new)

                self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
                self.openAction.setStatusTip("Open existing document")
                self.openAction.setShortcut("Ctrl+O")
                self.openAction.triggered.connect(self.open)

                self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
                self.saveAction.setStatusTip("Save document")
                self.saveAction.setShortcut("Ctrl+S")
                self.saveAction.triggered.connect(self.save)

                self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
                self.printAction.setStatusTip("Print document")
                self.printAction.setShortcut("Ctrl+P")
                self.printAction.triggered.connect(self.Print)

                self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
                self.previewAction.setStatusTip("Preview page before printing")
                self.previewAction.setShortcut("Ctrl+Shift+P")
                self.previewAction.triggered.connect(self.preview)

                self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
                self.cutAction.setStatusTip("Delete and copy text to clipboard")
                self.cutAction.setShortcut("Ctrl+X")
                self.cutAction.triggered.connect(self.text.cut)

                self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
                self.copyAction.setStatusTip("Copy text to clipboard")
                self.copyAction.setShortcut("Ctrl+C")
                self.copyAction.triggered.connect(self.text.copy)

                self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
                self.pasteAction.setStatusTip("Paste text from clipboard")
                self.pasteAction.setShortcut("Ctrl+V")
                self.pasteAction.triggered.connect(self.text.paste)

                self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
                self.undoAction.setStatusTip("Undo last action")
                self.undoAction.setShortcut("Ctrl+Z")
                self.undoAction.triggered.connect(self.text.undo)

                self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last action",self)
                self.redoAction.setStatusTip("Redo last action")
                self.redoAction.setShortcut("Ctrl+Y")
                self.redoAction.triggered.connect(self.text.redo)

                bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),"Insert bullet List",self)
                bulletAction.setStatusTip("Insert bullet list")
                bulletAction.setShortcut("Ctrl+Shift+B")
                bulletAction.triggered.connect(self.bulletList)

                numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered List",self)
                numberedAction.setStatusTip("Insert numbered list")
                numberedAction.setShortcut("Ctrl+Shift+L")
                numberedAction.triggered.connect(self.numberList)

                self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find and replace",self)
                self.findAction.setStatusTip("Find and replace words in your document")
                self.findAction.setShortcut("Ctrl+F")
                self.findAction.triggered.connect(find.Find(self).show)

                wordCountAction = QtGui.QAction(QtGui.QIcon("icons/count.png"),"See word/symbol count",self)
                wordCountAction.setStatusTip("See word/symbol count")
                wordCountAction.setShortcut("Ctrl+W")
                wordCountAction.triggered.connect(self.wordCount)

                imageAction = QtGui.QAction(QtGui.QIcon("icons/image.png"),"Insert image",self)
                imageAction.setStatusTip("Insert image")
                imageAction.setShortcut("Ctrl+Shift+I")
                imageAction.triggered.connect(self.insertImage)

                dateTimeAction = QtGui.QAction(QtGui.QIcon("icons/calender.png"),"Insert current date/time",self)
                dateTimeAction.setStatusTip("Insert current date/time")
                dateTimeAction.setShortcut("Ctrl+D")
                dateTimeAction.triggered.connect(datetime.DateTime(self).show)

                tableAction = QtGui.QAction(QtGui.QIcon("icons/table.png"),"Insert table",self)
                tableAction.setStatusTip("Insert table")
                tableAction.setShortcut("Ctrl+T")
                tableAction.triggered.connect(table.Table(self).show)

                self.toolbar = self.addToolBar("Options")

                self.toolbar.addAction(self.newAction)
                self.toolbar.addAction(self.openAction)
                self.toolbar.addAction(self.saveAction)

                self.toolbar.addSeparator()
                
                self.toolbar.addAction(self.printAction)
                self.toolbar.addAction(self.previewAction)

                self.toolbar.addSeparator()

                self.toolbar.addAction(self.cutAction)
                self.toolbar.addAction(self.copyAction)
                self.toolbar.addAction(self.pasteAction)
                self.toolbar.addAction(self.undoAction)
                self.toolbar.addAction(self.redoAction)

                self.toolbar.addSeparator()

                self.toolbar.addAction(self.findAction)
                self.toolbar.addAction(wordCountAction)
                self.toolbar.addAction(imageAction)

                self.toolbar.addSeparator()

                self.toolbar.addAction(bulletAction)
                self.toolbar.addAction(numberedAction)

                self.toolbar.addSeparator()

                self.toolbar.addAction(dateTimeAction)

                self.toolbar.addAction(tableAction)
                
                # Makes the next toolbar appear underneath this one
                self.addToolBarBreak()

        def initFormatbar(self):
                fontBox = QtGui.QFontComboBox(self)
                fontBox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))

                fontSize = QtGui.QSpinBox(self)

                # Will display " pt" after each value
                fontSize.setSuffix(" pt")

                fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))

                fontSize.setValue(14)

                fontColor = QtGui.QAction(QtGui.QIcon("icons/font-color.png"),"Change font color",self)
                fontColor.triggered.connect(self.fontColor)

                backColor = QtGui.QAction(QtGui.QIcon("icons/highlight.png"),"Change background color",self)
                backColor.triggered.connect(self.highlight)

                boldAction = QtGui.QAction(QtGui.QIcon("icons/bold.png"),"Bold",self)
                boldAction.triggered.connect(self.bold)

                italicAction = QtGui.QAction(QtGui.QIcon("icons/italic.png"),"Italic",self)
                italicAction.triggered.connect(self.italic)

                underlAction = QtGui.QAction(QtGui.QIcon("icons/underline.png"),"Underline",self)
                underlAction.triggered.connect(self.underline)

                strikeAction = QtGui.QAction(QtGui.QIcon("icons/strike.png"),"Strike-out",self)
                strikeAction.triggered.connect(self.strike)

                superAction = QtGui.QAction(QtGui.QIcon("icons/superscript.png"),"Superscript",self)
                superAction.triggered.connect(self.superScript)

                subAction = QtGui.QAction(QtGui.QIcon("icons/subscript.png"),"Subscript",self)
                subAction.triggered.connect(self.subScript)

                alignLeft = QtGui.QAction(QtGui.QIcon("icons/align-left.png"),"Align left",self)
                alignLeft.triggered.connect(self.alignLeft)

                alignCenter = QtGui.QAction(QtGui.QIcon("icons/align-center.png"),"Align left",self)
                alignCenter.triggered.connect(self.alignCenter)

                alignRight = QtGui.QAction(QtGui.QIcon("icons/align-right.png"),"Align right",self)
                alignRight.triggered.connect(self.alignRight)

                alignJustify = QtGui.QAction(QtGui.QIcon("icons/align-justify.png"),"Align justify",self)
                alignJustify.triggered.connect(self.alignJustify)

                indentAction = QtGui.QAction(QtGui.QIcon("icons/indent.png"),"Indent Area",self)
                indentAction.setShortcut("Ctrl+Tab")
                indentAction.triggered.connect(self.indent)

                dedentAction = QtGui.QAction(QtGui.QIcon("icons/dedent.png"),"Dedent Area",self)
                dedentAction.setShortcut("Shift+Tab")
                dedentAction.triggered.connect(self.dedent)
                
                self.formatbar = self.addToolBar("Format")
                self.formatbar.addWidget(fontBox)
                self.formatbar.addWidget(fontSize)

                self.formatbar.addSeparator()

                self.formatbar.addAction(fontColor)
                self.formatbar.addAction(backColor)
                self.formatbar.addAction(boldAction)
                self.formatbar.addAction(italicAction)
                self.formatbar.addAction(underlAction)
                self.formatbar.addAction(strikeAction)
                self.formatbar.addAction(superAction)
                self.formatbar.addAction(subAction)

                self.formatbar.addAction(alignLeft)
                self.formatbar.addAction(alignCenter)
                self.formatbar.addAction(alignRight)
                self.formatbar.addAction(alignJustify)

                self.formatbar.addAction(indentAction)
                self.formatbar.addAction(dedentAction)

                self.formatbar.addSeparator()

        def initMenubar(self):
                menubar = self.menuBar()
                file = menubar.addMenu("File")
                edit = menubar.addMenu("Edit")
                view = menubar.addMenu("View")

                file.addAction(self.newAction)
                file.addAction(self.openAction)
                file.addAction(self.saveAction)
                file.addAction(self.printAction)
                file.addAction(self.printAction)

                edit.addAction(self.undoAction)
                edit.addAction(self.redoAction)
                edit.addAction(self.cutAction)
                edit.addAction(self.copyAction)
                edit.addAction(self.pasteAction)

                edit.addAction(self.findAction) 

                # Toggling actions for the various bars
                toolbarAction = QtGui.QAction("Toggle Toolbar",self)
                toolbarAction.triggered.connect(self.toggleToolbar)

                formatbarAction = QtGui.QAction("Toggle Formatbar",self)
                formatbarAction.triggered.connect(self.toggleFormatbar)

                statusbarAction = QtGui.QAction("Toggle Statusbar",self)
                statusbarAction.triggered.connect(self.toggleStatusbar)

                view.addAction(toolbarAction)
                view.addAction(formatbarAction)
                view.addAction(statusbarAction)

        def initUI(self):
                self.text = QtGui.QTextEdit(self)
                self.setCentralWidget(self.text)
                self.initToolbar()
                self.initFormatbar()
                self.initMenubar()
                #Initialize a statusbar for the window
                self.statusbar = self.statusBar()
                # x and y coords on screen, width, height
                self.setGeometry(100,100,940,800)
                self.setWindowTitle("Writer")
                self.text.setTabStopWidth(30)
                self.setWindowIcon(QtGui.QIcon("icons/icon.png"))
                self.text.cursorPositionChanged.connect(self.cursorPosition)
                self.text.textChanged.connect(self.changed)

        def new(self):
                spawn = Main(self)
                spawn.show()

        def open(self):
                # Get filename and show only .writer files
                self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',".","(*.writer)")

                if self.filename:
                        with open(self.filename,"rt") as file:
                                self.text.setText(file.read())

        def save(self):
                # Only open dialog if there is no filename yet
                if not self.filename:
                        self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

                # Append extension if not there yet
                if not self.filename.endsWith(".writer"):
                        self.filename += ".writer"

                # We just store the contents of the text filealong with the
                # format in html, which Qt does in a very nice way for us
                with open(self.filename,"wt") as file:
                        file.write(self.text.toHtml())

        def preview(self):
                # Open preview dialog
                preview = QtGui.QPrintPreviewDialog()

                # If a print is requested, open print dialog
                preview.paintRequested.connect(lambda p: self.text.print_(p))

                preview.exec_()

        def Print(self):

                # Open printing dialog
                dialog = QtGui.QPrintDialog()

                if dialog.exec_() == QtGui.QDialog.Accepted:
                        self.text.document().print_(dialog.printer())

        def bulletList(self):
                cursor = self.text.textCursor()
                # Insert bulleted list
                cursor.insertList(QtGui.QTextListFormat.ListDisc)

        def numberList(self):
                cursor = self.text.textCursor()
                # Insert list with numbers
                cursor.insertList(QtGui.QTextListFormat.ListDecimal)

        def cursorPosition(self):
                cursor = self.text.textCursor()
                # Mortals like 1-indexed things
                line = cursor.blockNumber() + 1
                col = cursor.columnNumber()

                self.statusbar.showMessage("Line: {} | Column ()".format(line,col))

        def fontFamily(self,font):
                self.text.setCurrentFont(font)

        def fontSize(self,fontsize):
                self.text.setFontPointSize(int(fontsize + 1))

        def fontColor(self):

                # Get a color from the text dialog
                color = QtGui.QColorDialog.getColor()

                # Set it as a new text color
                self.text.setTextColor(color)

        def highlight(self):
                color = QtGui.QColorDialog.getColor()
                self.text.setTextBackgroundColor(color)

        def bold(self):
                if self.text.fontWeight() == QtGui.QFont.Bold:
                        self.text.setFontWeight(QtGui.QFont.Normal)
                else:
                        self.text.setFontWeight(QtGui.QFont.Bold)

        def italic(self):
                state = self.text.fontItalic()
                self.text.setFontItalic(not state)

        def underline(self):
                state = self.text.fontUnderline()
                self.text.setFontUnderline(not state)

        def strike(self):
                # Grab the text's format
                fmt =self.text.currentCharFormat()

                # Set the fontStrikeOut property to its opposite
                fmt.setFontStrikeOut(not fmt.fontStrikeOut())

                # And set the next char format
                self.text.setCurrentCharFormat(fmt)

        def superScript(self):
                # Grab the current format
                fmt = self.text.currentCharFormat()

                # And get the vertical alignment property
                align = fmt.verticalAlignment()

                # Toggle the state
                if align == QtGui.QTextCharFormat.AlignNormal:
                        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
                else:
                        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
                # Set the new format
                self.text.setCurrentCharFormat(fmt)

        def subScript(self):
                #Grab the current format
                fmt = self.text.currentCharFormat()

                # And get the vertical alignment property
                align = fmt.verticalAlignment()

                # Toggle the state
                if align == QtGui.QTextCharFormat.AlignNormal:
                        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
                else:
                        fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

                # Set the new format
                self.text.setCurrentCharFormat(fmt)

        def alignLeft(self):
                self.text.setAlignment(Qt.AlignLeft)

        def alignCenter(self):
                self.text.setAlignment(Qt.AlignCenter)

        def alignRight(self):
                self.text.setAlignment(Qt.AlignRight)

        def alignJustify(self):
                self.text.setAlignment(Qt.AlignJustify)

        def indent(self):
                # Grab the cursor
                cursor = self.text.textCursor()

                if cursor.hasSelection():
                        # Store the current line/block number
                        temp = cursor.blockNumber()

                        # Move to the selection's last line
                        cursor.setPosition(cursor.selectionEnd())

                        # Calculate the range of selection
                        diff = cursor.blockNumber() - temp

                        # Iterate over lines
                        for n in range(diff + 1):

                                # Move to start of each line
                                cursor.movePosition(QtGui.QtextCursor.StartOfLine)

                                # Insert tabbing
                                cursor.insertText("\t")

                                # And move back up
                                cursor.movePosition(QtGui.QTextCursor.Up)

                # If there is no selection, just insert a tab
                else:
                        cursor.insertText("\t")

        def dedent(self):
                # Grab the cursor
                cursor = self.text.textCursor()

                if cursor.hasSelection():
                        # Store the current line/block number
                        temp = cursor.blockNumber()

                        # Move to the selection's last line
                        cursor.setPosition(cursor.selectionEnd())

                        # Calculate the range of selection
                        diff = cursor.blockNumber() - temp

                        # Iterate over lines
                        for n in range(diff + 1):
                                self.handleDedent(cursor)
                                # Move up
                                cursor.movePosition(QtGui.QTextCursor.Up)
                else:
                        self.handleDedent(cursor)

        def handleDedent(self,cursor):
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)

                # Grab the current line
                line = cursor.block().text()

                # If the line starts with a tab character, deleteit
                if line.startsWith("\t"):

                        # Delete next character
                        cursor.deleteChar()

                # Otherwise, delete all spaces until a non-space character is met
                else:
                        for char in line[:8]:
                                if char != " ":
                                        break
                                cursor.deleteChar()

        def toggleToolbar(self):
                state = self.toolbar.isVisible()
                # Set the visibility to its inverse
                self.toolbar.setVisible(not state)

        def toggleFormatbar(self):
                state = self.formatbar.isVisible()
                # Set the visibility to its inverse
                self.formatbar.setVisible(not state)
                        
        def toggleStatusbar(self):
                state = self.statusbar.isVisible()
                # Set the visibility to its inverse
                self.statusbar.setVisible(not state)

        def insertImage(self):
                # Get image file name
                filename = QtGui.QFileDialog.getOpenFileName(self, 'Insert image',".","Images(*.png *.xpm *.jpg *.bmp *.gif)")

                # Create image object
                image = QtGui.QImage(filename)

                # Error if unloadable
                if image.isNull():

                        popup = QtGui.QMessageBox(QtGui.QMessageBox.Critical,
                                                  "Image load error",
                                                  "Could not load image file!",
                                                  QtGui.QMessageBox.Ok,
                                                  self)

                        popup.show()
                else:
                        cursor = self.text.textCursor()
                        cursor.insertImage(image,filename)

        def wordCount(self):
                wc = wordcount.WordCount(self)
                wc.getText()
                wc.show()
        
        def context(self,pos):
                # Grab the cursor
                cursor = self.text.textCursor()

                # Grab the current table, if there is one
                table = cursor.currentTable()

                # Above will return 0 if there is no current table, in which case
                # we call the normal context menu. If there is a table, we create
                # our own context menu specific to table interaction
                if table:

                    menu = QtGui.QMenu(self)

                    appendRowAction = QtGui.QAction("Append row",self)
                    appendRowAction.triggered.connect(lambda: table.appendRows(1))

                    appendColAction = QtGui.QAction("Append column",self)
                    appendColAction.triggered.connect(lambda: table.appendColumns(1))


                    removeRowAction = QtGui.QAction("Remove row",self)
                    removeRowAction.triggered.connect(self.removeRow)

                    removeColAction = QtGui.QAction("Remove column",self)
                    removeColAction.triggered.connect(self.removeCol)


                    insertRowAction = QtGui.QAction("Insert row",self)
                    insertRowAction.triggered.connect(self.insertRow)

                    insertColAction = QtGui.QAction("Insert column",self)
                    insertColAction.triggered.connect(self.insertCol)


                    mergeAction = QtGui.QAction("Merge cells",self)
                    mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

                    # Only allow merging if there is a selection
                    if not cursor.hasSelection():
                        mergeAction.setEnabled(False)


                    splitAction = QtGui.QAction("Split cells",self)

                    cell = table.cellAt(cursor)

                    # Only allow splitting if the current cell is larger
                    # than a normal cell
                    if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                        splitAction.triggered.connect(lambda: table.splitCell(cell.row(),cell.column(),1,1))

                    else:
                        splitAction.setEnabled(False)


                    menu.addAction(appendRowAction)
                    menu.addAction(appendColAction)

                    menu.addSeparator()

                    menu.addAction(removeRowAction)
                    menu.addAction(removeColAction)

                    menu.addSeparator()

                    menu.addAction(insertRowAction)
                    menu.addAction(insertColAction)

                    menu.addSeparator()

                    menu.addAction(mergeAction)
                    menu.addAction(splitAction)

                    # Convert the widget coordinates into global coordinates
                    pos = self.mapToGlobal(pos)

                    # Add pixels for the tool and formatbars, which are not included
                    # in mapToGlobal(), but only if the two are currently visible and
                    # not toggled by the user

                    if self.toolbar.isVisible():
                        pos.setY(pos.y() + 45)

                    if self.formatbar.isVisible():
                        pos.setY(pos.y() + 45)

                    # Move the menu to the new position
                    menu.move(pos)

                    menu.show()

                else:

                    event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse,QtCore.QPoint())

                    self.text.contextMenuEvent(event)
        
        def removeRow(self):

                # Grab the cursor
                cursor = self.text.textCursor()

                # Grab the current table (we assume there is one, since
                # this is checked before calling)
                table = cursor.currentTable()

                # Get the current cell
                cell = table.cellAt(cursor)

                # Delete the cell's row
                table.removeRows(cell.row(),1)

        def removeCol(self):

                # Grab the cursor
                cursor = self.text.textCursor()

                # Grab the current table (we assume there is one, since
                # this is checked before calling)
                table = cursor.currentTable()

                # Get the current cell
                cell = table.cellAt(cursor)

                # Delete the cell's column
                table.removeColumns(cell.column(),1)

        def insertRow(self):

                # Grab the cursor
                cursor = self.text.textCursor()

                # Grab the current table (we assume there is one, since
                # this is checked before calling)
                table = cursor.currentTable()

                # Get the current cell
                cell = table.cellAt(cursor)

                # Insert a new row at the cell's position
                table.insertRows(cell.row(),1)

        def insertCol(self):

                # Grab the cursor
                cursor = self.text.textCursor()

                # Grab the current table (we assume there is one, since
                # this is checked before calling)
                table = cursor.currentTable()

                # Get the current cell
                cell = table.cellAt(cursor)

                # Insert a new row at the cell's position
                table.insertColumns(cell.column(),1)

        def changed(self):
                self.changesSaved = False

        def closeEvent(self, event):
                if self.changesSaved:
                        event.accept()
                else:
                        popup = QtGui.QMessageBox(self)
                        popup.setIcon(QtGui.QMessageBox.Warning)
                        popup.setText("The document has been modified")
                        popup.setInformativeText("Do you want to save your changes?")
                        popup.setStandardButtons(QtGui.QMessageBox.Save   |
                                                 QtGui.QMessageBox.Cancel |
                                                 QtGui.QMessageBox.Discard)
                        popup.setDefaultButton(QtGui.QMessageBox.Save)
                        answer = popup.exec_()
                        if answer == QtGui.QMessageBox.Save:
                                self.save()
                        elif answer == QtGui.QMessageBox.Discard:
                                event.accept()
                        else:
                                event.ignore()
                                   
def main():
        app = QtGui.QApplication(sys.argv)
        main = Main()
        main.show()
        sys.exit(app.exec_())
        
if __name__== "__main__":
        main()
 
