# Tag와 Release

프로젝트에서 첫 완성본이나 실험 결과를 다시 찾으려면 긴 커밋 해시 대신 기억하기 쉬운 이름을 붙일 수 있음. Git의 태그는 특정 커밋을 가리키는 이름이며, GitHub Release는 태그를 바탕으로 설명과 배포 파일을 정리하는 기능임.

## 브랜치와 태그의 차이

브랜치는 그 위에서 새 커밋을 만들면 최신 커밋을 가리키도록 이동함. 태그는 특정 커밋을 가리키는 이름으로, 따로 변경하지 않으면 새 커밋이 생겨도 기존 위치에 남음. 태그를 붙인다고 새 커밋이 만들어지는 것은 아님.

태그가 가리키는 것은 해당 시점의 저장소 전체 상태임. 특정 미니프로젝트의 이름을 태그에 붙였더라도 한 폴더만 따로 기록한 버전은 아님. 예를 들어 `mini-01-v1.0.0`은 이름을 붙인 시점의 전체 커밋을 가리킴.

## 태그를 만들고 원격에 올리기

아래는 현재 커밋에 설명이 있는 annotated tag를 붙이는 예시임. 이미 같은 이름의 태그가 있는지 먼저 확인함.

```powershell
git tag
git tag -a v1.0.0 -m "첫 학습 기록 버전"
git show v1.0.0
git push origin v1.0.0
```

`git show`로 어떤 커밋을 가리키는지 확인하고, 마지막 명령으로 지정한 태그를 원격에 전송함. 브랜치에 대한 일반 push가 모든 태그까지 자동으로 올리는 것은 아님.

GitHub에서 해당 태그를 선택하고 변경 설명과 필요한 배포 파일을 작성해 Release를 만들 수 있음. 태그 push와 Release 작성은 별도 단계임. 커밋은 프로젝트 상태를 기록하고 태그는 그 커밋을 찾기 쉬운 이름으로 가리키며 Release는 배포 내용을 설명함.

## 버전 번호의 의미

Semantic Versioning은 공개 API의 호환성을 기준으로 `MAJOR.MINOR.PATCH`를 정하는 규칙임. `1.4.2`라면 1이 MAJOR, 4가 MINOR, 2가 PATCH임.

| 자리 | 올리는 경우 |
| --- | --- |
| MAJOR | 기존 사용 방식과 호환되지 않는 변경 |
| MINOR | 기존 호환성을 유지하는 기능 추가 |
| PATCH | 호환성을 유지하는 오류 수정 |

상위 자리를 올리면 그 아래 숫자는 0으로 초기화함. `0.y.z`는 초기 개발 단계로 변경 가능성이 큼. 버전 번호가 높다는 것은 변경을 구분하는 정보이며 모델 성능이 반드시 더 좋다는 뜻은 아님. 실험 결과와 변경 목적을 함께 기록해야 비교할 수 있음.

참고: [git tag](https://git-scm.com/docs/git-tag), [GitHub Release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), [SemVer](https://semver.org/lang/ko/)

[이전](03-pull-request.md) | [목차로](../README.md)
