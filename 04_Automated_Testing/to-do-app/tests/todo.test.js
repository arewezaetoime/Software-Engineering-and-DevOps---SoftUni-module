const { test, expect } = require('@playwright/test');

test('Checking user add a task', async({ page }) => {
    await page.goto('http://127.0.0.1:5500/04_Automated_Testing/to-do-app/index.html');
    await page.fill('#task-input', 'Test Task');
    await page.click('#add-task');

    const taskText = await page.textContent('.task');
    expect(taskText).toContain('Test Task');
});

test('User delete task', async ({ page }) => {
    await page.goto('http://127.0.0.1:5500/04_Automated_Testing/to-do-app/index.html')
    await page.fill('#task-input', 'delete task')
    await page.click('#add-task')
    
    // Delete the task deiba
    await page.click('.task .delete-task');

    const tasks = await page.$$eval('.task',
        tasks => tasks.map(task => task.textContent));
    expect(tas).not.toContain('delete task');
})

test('User can complete task', async ({ page }) => {
    await page.goto('http://127.0.0.1:5500/04_Automated_Testing/to-do-app/index.html')
    await page.fill('#task-input', 'complete task')
    await page.click('#add-task')
    
    // Delete the task deiba
    await page.click('.task .complete-task');

    const completedTasks = await page.$('.task.completed');
    expect(completedTasks).not.toBeNull();
})

test('USer can filter tasks', async ({ page }) => {
    await page.goto('http://127.0.0.1:5500/04_Automated_Testing/to-do-app/index.html')
    await page.fill('#task-input', 'filter task')
    await page.click('#add-task')

    await page.click('.task .task-complete');
    const incompleteTask = await page.$('.task:not(.completed)')
    expect(incompleteTask).toBeNull();
})