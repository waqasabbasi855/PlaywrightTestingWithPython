class ProjectsPage:
    project = "//span[text()='Cross-functional project plan']"
    board = "(//span[text()='Board'])[2]"
    addtask = "//div[text()='Add task']"
    nameoftask = "(//textarea)[1]"
    priority = "//span[text()='Priority']"
    status = "//span[text()='Status']"

    async def ClickOnProject(page):
        projectclick=await page.query_selector(ProjectsPage.project)
        await projectclick.click()

    async def ClickonBoard(page):
        clickboard=await page.query_selector(ProjectsPage.board)
        await clickboard.click()

    async def Addtaskbtn(page):
        addtask=await page.query_selector(ProjectsPage.addtask)
        await addtask.click()

    async def Taskname(page, taskname):
        tasknamefill=await page.query_selector(ProjectsPage.nameoftask)
        await tasknamefill.fill(taskname)

    async def Priorityoftask(page):

        dropdown = await page.query_selector(ProjectsPage.priority)
        await dropdown.click()
        await dropdown.type("low")
        await dropdown.press("Enter")

    async def Statusoftask(page):
        dropdown = await page.query_selector(ProjectsPage.status)
        await dropdown.click()
        await dropdown.type("at")
        await dropdown.press("Enter")


