/*
*网站普遍js功能
*/
function toDesktop(sUrl,sName){ 
try{ 
var WshShell = new ActiveXObject("WScript.Shell"); 
var oUrlLink = WshShell.CreateShortcut(WshShell.SpecialFolders("Desktop") + "\\" + sName + ".url"); 
oUrlLink.TargetPath = sUrl; 
oUrlLink.Save(); 
}catch(e){ 
alert("当前IE安全级别不允许操作！"); 
} 
} 
