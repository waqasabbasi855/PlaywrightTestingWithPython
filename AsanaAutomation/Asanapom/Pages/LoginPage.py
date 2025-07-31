class login:
    loginbtn = "//span[text()='Log In']"
    useremailfield = "//input[@type='email']"
    continuebutton = "//div[text()='Continue']"
    userpasswordfield = "//input[@type='password']"
    loginButton = "//div[text()='Log in']"

    async def Loginclick(page):
        homeloginelement = await page.query_selector(login.loginbtn)
        await homeloginelement.click()

    async def Emailfield(page, mail):
        emailfieldelement = await page.query_selector(login.useremailfield)
        await emailfieldelement.fill(mail)

    async def Continue_Email(page):
        continuebuttonelement=await page.query_selector(login.continuebutton)
        await continuebuttonelement.click()

    async def passwordfield(page, passwordoffield):
        passwordfieldelement=await page.query_selector(login.userpasswordfield)
        await passwordfieldelement.fill(passwordoffield)

    async def Final_Login_Button(page):
        finalbuttonelement=await page.query_selector(login.loginButton)
        await finalbuttonelement.click()


