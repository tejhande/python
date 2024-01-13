import pyautogui
import time

time.sleep(3) # Give you time to switch to the Excel window

# Define an array of column letters from A to ZZ
cols = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
cols += [f"A{c}" for c in cols]

# Loop over rows 1 to 10
for row in range(1, 11):
    # Loop over columns A to ZZ
    for col in cols:
        # Combine the column letter and the row number to form the cell name
        cell = col + str(row)

        # Type the cell name in the current cell and move to the next cell
        pyautogui.typewrite(cell)   
        pyautogui.press("tab")

        # If we've reached the last column, press Enter to move to the next row
        if col == "ZZ":
            pyautogui.press("enter")
