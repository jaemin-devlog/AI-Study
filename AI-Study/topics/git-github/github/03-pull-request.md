# Fork와 Pull Request

## PR

- 작업 브랜치의 변경을 다른 브랜치에 합쳐 달라는 요청
- 변경 내용 검토·의견 교환 후 병합
- PR 생성과 병합은 별도

| 항목 | 의미 | 브랜치 |
| --- | --- | --- |
| base | 변경을 받을 브랜치 | `main` |
| compare / head | 내 작업이 있는 브랜치 | `docs/git-note` |

작업 브랜치 전송:

```powershell
git push -u origin docs/git-note
```

- 같은 브랜치에 추가 commit·push하면 기존 PR에 반영
- 같은 저장소의 브랜치끼리도 PR 가능. fork는 필수 아님

## Fork와 Clone

| 구분 | 복사본 위치 |
| --- | --- |
| Fork | 내 GitHub 계정 |
| Clone | 내 컴퓨터 |

- 원본에 push 권한이 없을 때: fork가 허용된 저장소를 내 계정으로 복사
- 내 fork에 push한 변경을 원본 저장소로 PR 요청
- 공개 코드의 재사용 권한은 라이선스로 확인

## 병합 후 로컬 main

```powershell
git switch main
git pull --ff-only origin main
```

- GitHub에서 병합해도 로컬 main은 자동 갱신되지 않음
- 작업 브랜치 삭제 전 반영 여부 확인
- squash·rebase 병합 후에는 `git branch -d`가 거절될 수도 있음

참고: [PR 만들기](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request), [Fork](https://docs.github.com/en/pull-requests/reference/forks)

[목차로](../README.md)
