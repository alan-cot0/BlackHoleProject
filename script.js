/**
 * This function tests a sample bit of Python code. (Deprecated)
 * @param none
 */
async function testPythonScript() {
    const elementID = document.getElementById("output1");
    const pyodide2 = await loadPyodide();
    console.log(pyodide2.runPython(`print(5)`));
    elementID.textContent = pyodide2.runPython(`print("It worked!")`);
}