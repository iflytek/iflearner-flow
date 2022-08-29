# Iflearn Flow Federate Errcode API    
# CommonError
|     ret_module      | ret_code |        ret_msg        |
| ------------------- | -------: | --------------------- |
| RequestParamResonse |    10000 | request param invalid |
    
# FederateError
|       ret_module       | ret_code |           ret_msg            |
| ---------------------- | -------: | ---------------------------- |
| FederateRepeatRegister |    10100 | federate has been registered |
    
# Success
|   ret_module    | ret_code | ret_msg |
| --------------- | -------: | ------- |
| SuccessResponse |        0 | success |
    
# TaskError
|     ret_module      | ret_code |       ret_msg        |
| ------------------- | -------: | -------------------- |
| TaskNameDuplicate   |    10301 | duplicate task name  |
| TaskNameEmpty       |    10302 | empty task name      |
| TaskNotFound        |    10300 | task not found       |
| TaskPartyNotFound   |    10304 | task party not found |
| TaskStatusConflicit |    10303 | status conflicit     |
    
# TemplateError
|    ret_module     | ret_code |         ret_msg         |
| ----------------- | -------: | ----------------------- |
| TemplateNameEmpty |    10202 | empty template name     |
| TemplateNotFound  |    10200 | template not found      |
| TemplateRepeat    |    10201 | duplicate template name |
    
