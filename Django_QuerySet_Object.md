# Django에서 Queryset과 Object
* 장고에서 .get('key':value)로 데이터를 가져오면 object 형식, .filter('key':value)는 queryset 형식
* get 할 때 해당 데이터가 없다면 에러, queryset은 데이터가 존재하지 않더라도 빈 리스트로 가져와햣 정상 작동
* .get 은 try 예외 처리를 함께 작성해 주어야 데이터가 존재하지 않을 때 에러를 방지할 수 있다
* .filter는 빈 리스트를 가져 오는 경우를 따로 처리함으로써 기능을 보완할 수 있다
