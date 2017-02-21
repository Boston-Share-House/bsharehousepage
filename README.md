# bsharehousepage

## 実行サーバーを同期させる方法

```
$ git config --edit
```

```.git/config
...
[remote "origin"]
  url = https://github.com/boston-share-house/bsharehousepage
  url = {server-hostname}:{git-proj-path} #（ここはSlackか何かで聞いてください）
  fetch = ...
...
```

```
$ git push -u origin master
```

もしくは:

```.git/config
...
[remote "production"]
  url = {server-hostname}:{git-proj-path}
  fetch = ...
...
```
にする。
