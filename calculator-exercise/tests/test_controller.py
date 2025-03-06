# def test_returnSignal(controller):
#     """Tests the Return key binding interface to our Qt display widget."""
#     from PyQt5 import QtCore, QtGui

#     controller._view.setDisplayText("1+2")
#     event = QtGui.QKeyEvent(
#         QtCore.QEvent.KeyPress, QtCore.Qt.Key_Enter, QtCore.Qt.NoModifier
#     )
#     controller._view.display.keyPressEvent(event)
#     assert controller._view.displayText() == "3"


# def test_evalExpression(model):
#     assert model("1 + 2") == "3"

# import pytest

# @pytest.mark.parametrize(
#         "expression, expected_result",
#         [
#             ("1 + 2", "3"),
#             ("1 + 2", "22")
#         ]
# )
# def test_calculateResult(controller, expression, expected_result):
#     """Tests the function of _calculateResult."""
#     controller._view.setDisplayText(expression)
#     controller._calculateResult()
#     assert controller._view.displayText() == expected_result
