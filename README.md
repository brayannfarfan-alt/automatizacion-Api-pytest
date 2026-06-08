secret key: free_user_3DlMlTJEai0AWD9gw6DvADtOxi6

pytest -v --html=reports/report.html --self-contained-html


from pathlib import Path
Path("screenshots").mkdir(exist_ok=True)

@pytest.hookimpl(hookwrapper=True) #HOOK
def pytest_runtest_makereport(item, call):

    # SETUP
    # CALL
    # Teardown

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            driver.save_screenshot(
                f"screenshots/{item.name}.png" #configuracion de como se va a llamar mi captura
            )
