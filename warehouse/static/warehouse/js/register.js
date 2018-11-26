function all_confirm()
{
    if(document.form.account.value == null ||
        document.form.account.value == "")
    {
        alert("帐号不能为空！");
        return false;
    }
    if(document.form.name.value == null ||
        document.form.name.value == "")
    {
        alert("昵称不能为空！");
        return false;
    }
    if(document.form.password.value == null ||
        document.form.password.value == null)
    {
        alert("密码不能为空！");
        return false;
    }
    document.form.account.focus()
}