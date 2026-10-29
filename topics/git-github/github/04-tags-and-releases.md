# Tag와 Release

- Tag: 특정 커밋에 붙이는 이름
- 브랜치는 새 커밋을 만들면 이동. 태그는 따로 바꾸지 않으면 같은 위치 유지
- Release: 태그를 기준으로 변경 설명·배포 파일을 묶는 GitHub 기능

## 태그 만들기

현재 커밋을 가리키는 `v1.0.0` 태그

```powershell
git tag -a v1.0.0 -m "Git 학습 노트 첫 버전"
git show v1.0.0
git push origin v1.0.0
```

- `-a`: 설명을 남기는 annotated tag
- 일반 브랜치 push에 모든 태그가 포함되는 것은 아님. 필요한 태그를 따로 push
- GitHub에서 태그 선택 후 Release 생성. 태그 push와는 별도

## 버전 숫자 읽기

SemVer: 공개 API의 호환성을 기준으로 `MAJOR.MINOR.PATCH`를 정하는 규칙

| 자리 | 올리는 경우 |
| --- | --- |
| MAJOR | 이전 방식과 호환되지 않게 바꿨을 때 |
| MINOR | 호환성을 유지하면서 기능을 추가했을 때 |
| PATCH | 호환성을 유지하면서 버그를 고쳤을 때 |

- `1.4.2`: MAJOR 1 / MINOR 4 / PATCH 2
- 위 자리를 올릴 때 아래 숫자는 0으로 초기화
- `0.y.z`: 초기 개발 단계. API 변경 가능

참고: [git tag](https://git-scm.com/docs/git-tag), [GitHub Release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), [SemVer](https://semver.org/lang/ko/)

[목차로](../README.md)
