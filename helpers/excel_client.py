from __future__ import annotations

from typing import Any, Optional

import openpyxl
from openpyxl.cell import Cell
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class ExcelClient:
    """
    Args:
        file_path: str - path to the xlsx file
        read_only: bool - read-only mode
        pure_data: bool - get pure data from cells
    """

    def __init__(self, file_path: str, read_only: bool = False, pure_data: bool = False) -> None:
        self.file_path = file_path
        self._file = openpyxl.load_workbook(filename=file_path, read_only=read_only, data_only=pure_data)

    def __enter__(self) -> ExcelClient:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self._file.close()

    @property
    def excel_file(self) -> Workbook:
        return self._file

    def get_work_sheet(self, work_sheet_name: str) -> Worksheet:
        return self.excel_file[work_sheet_name]

    def save_excel_file(self, path_to_save: str) -> None:
        self.excel_file.save(path_to_save)

    def compare_sheets_in_excel_file(self, file_path_2: str, sheet_name_file_1: str, sheet_name_file_2: Optional[str] = None) -> list[str]:
        """Compare sheets from different xlsx files and check if they are identical"""
        errors = []
        if not sheet_name_file_2:
            sheet_name_file_2 = sheet_name_file_1
        with ExcelClient(file_path=file_path_2, read_only=True) as workbook_2:
            list_1 = self.get_work_sheet(sheet_name_file_1)
            list_2 = workbook_2.get_work_sheet(sheet_name_file_2)
            for row1, row2 in zip(list_1.rows, list_2.rows):
                for cell1, cell2 in zip(row1, row2):
                    if cell1.value != cell2.value:
                        errors.append(
                            f'Cell {cell1} from file {self.file_path} does not equal to {cell2} from file {file_path_2}'
                            f'. {cell1.value} != {cell2.value}'
                        )
        return errors

    def get_cells(self, sheet_name: str, start: str = 'A1', end: str = 'P10') -> list[Cell]:
        """Get list of cells with a specified range"""
        sheet = self.get_work_sheet(sheet_name)
        cell_range = sheet[start: end]
        return [cell for row in cell_range for cell in row]

    def get_worksheets(self) -> list[str]:
        """Get the list of worksheet names"""
        worksheet_names = self.excel_file.sheetnames
        return worksheet_names

    def change_worksheet_title(self, sheet_name: str, new_sheet_name: str) -> None:
        """Change the worksheet title"""
        self.get_work_sheet(sheet_name).title = new_sheet_name
        self.excel_file.save(self.file_path)

