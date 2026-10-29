# Stash

미커밋 변경 임시 보관. 나중에 다시 적용 가능.

## 수정 중인 내용 보관

기존 커밋 필요. 기본 보관 대상은 추적 파일의 수정 내용과 스테이지.

```powershell
git status
git stash push -m "Git 노트 작성 중"
```

- 보관한 변경을 작업 폴더에서 치우고 현재 커밋 상태로 복귀
- 미추적 파일은 기본 보관 대상에서 제외

미추적 파일 포함: `-u` 추가.

```powershell
git stash push -u -m "새 노트까지 임시 보관"
```

`-u`에도 `.gitignore`로 무시한 파일은 미포함.

## 보관한 내용 확인

```powershell
git stash list
git stash show -p "stash@{0}"
```

`stash@{0}`은 가장 최근 항목. PowerShell에서는 따옴표로 감싸서 사용.

## 다시 꺼내기

적용 전 현재 작업 정리.

| 명령 | 적용 후 stash 목록 |
| --- | --- |
| `git stash apply "stash@{0}"` | 항목 유지 |
| `git stash pop "stash@{0}"` | 적용 성공 시 항목 삭제 |

- 다른 브랜치에서도 적용 가능. 파일 내용에 따라 충돌 가능
- 충돌 시 stash 항목 유지
- 기존 스테이지 상태까지 복원하려면 `--index` 옵션 사용

`pop` 충돌 해결: 파일 수정·저장 → `git add`로 해결 표시 → 결과 확인 → 해당 stash 삭제.

```powershell
git add topics/git-github/README.md
git status
```

충돌 해결 결과와 삭제할 stash 번호 확인 후 `drop`.

```powershell
git stash list
git stash drop "stash@{0}"
```

참고: [Git stash](https://git-scm.com/docs/git-stash)

[목차로](../README.md)
