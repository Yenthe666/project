# Project
Apps related to Odoo it's project features:
- [project_stage_update](#project_stage_update): automatically update a project it's stages when the last task moves out of a project task stage.

## project_stage_update
Adds support to configure on a task stage to which stage the above project should automatically move.<br/>
This is done by configuring on the project task stage level a project stage:
![image](https://user-images.githubusercontent.com/6352350/219587821-4988f5e2-8c58-4562-a76a-05b90d2c8784.png)
In the above sample the project would move to the stage "In progress" when the last task moves out of the stage "backlog" for this project.
