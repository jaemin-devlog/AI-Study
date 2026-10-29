# 변경 되돌리기

미커밋 작업 보존: 되돌리기 전 파일 사본·stash로 보관.

```powershell
git status
git diff
git diff --staged
```

## 스테이지만 취소

전제: 첫 커밋 생성 후 `topics/git-github/README.md` 수정·`add`.

```powershell
git restore --staged topics/git-github/README.md
```

- 스테이지: 현재 커밋(`HEAD`) 기준으로 복원
- 작업 파일의 수정 내용: 유지
- 첫 커밋 전: `HEAD`가 없어서 사용 불가

## 파일 수정 내용 버리기

```powershell
git restore topics/git-github/README.md
```

- 작업 파일: 스테이지(index) 기준으로 복원. 아직 add하지 않은 수정은 삭제
- 스테이지와 마지막 커밋이 같을 때: 마지막 커밋 상태로 복원
- 추적 파일 삭제 후 아직 add하지 않은 경우: 파일 복원 가능

스테이지·작업 파일 모두 마지막 커밋 기준으로 복원:

```powershell
git restore --source=HEAD --staged --worktree topics/git-github/README.md
```

- 해당 파일의 staged·unstaged 변경 모두 삭제
- Untracked 파일: Git에 복원할 이전 기록 없음

## 로컬 커밋 위치 바꾸기

전제: 브랜치에서 작업 중, 커밋 두 개 이상.
`HEAD~1`: 현재 커밋의 첫 번째 부모.

| 명령 | 현재 브랜치 | 스테이지 | 작업 파일 |
| --- | --- | --- | --- |
| `git reset --soft HEAD~1` | 이전 커밋으로 이동 | 유지 | 유지 |
| `git reset --mixed HEAD~1` | 이전 커밋으로 이동 | 이전 커밋 상태 | 유지 |
| `git reset --hard HEAD~1` | 이전 커밋으로 이동 | 이전 커밋 상태 | 이전 커밋 상태 |

- 기본값: `--mixed`
- `--hard`: 추적 파일의 미커밋 변경까지 삭제
- 복원을 가로막는 Untracked 파일도 삭제 가능. 중요한 파일은 별도 보관
- 커밋 객체가 즉시 영구 삭제되지는 않지만, 복구를 전제로 사용하지 않기

## 공유한 커밋의 변경 취소

- 공유한 이력: `revert` 우선 사용
- 기존 커밋 유지, 변경을 취소하는 새 커밋 생성
- 실행 전: 미커밋 변경 정리, `git log --oneline`으로 취소 대상 확인

```powershell
git revert --no-edit HEAD
```

- `git revert --no-edit HEAD`: 현재 일반 커밋의 변경 취소
- 특정 커밋 취소: `HEAD` 위치에 해당 해시 지정
- Merge commit 취소: 부모 선택 옵션 필요
- 충돌: 파일 수정·`add` 후 `git revert --continue`
- 취소 작업 중단: `git revert --abort`

참고: [git restore](https://git-scm.com/docs/git-restore), [git reset](https://git-scm.com/docs/git-reset), [git revert](https://git-scm.com/docs/git-revert)

[목차로](../README.md)
