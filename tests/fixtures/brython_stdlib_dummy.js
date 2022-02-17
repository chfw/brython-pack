__BRYTHON__.use_VFS = true;
var scripts = {
  "testmodule": [".py", "print(\"hello world\")"],
  "testjs": [".js", "console.log(\"hello world\");"]
}
__BRYTHON__.update_VFS(scripts)
