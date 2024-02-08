# GraphDB について

## REST APIからqueryの実行

paramsに `"name": <query_name>` と `"query": <query_string>` を入れて、
`<base_url>/repositories/<repo_id>` に対してGETすると、クエリの返答が返ってくる。

Saved Queryを実行したいときは、Saved Queryをとってきて、その内容をパラメーターに`<query_string>`として入れる。
