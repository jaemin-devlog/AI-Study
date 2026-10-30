# 변경 되돌리기

되돌리려는 내용이 어디까지 기록됐는지에 따라 명령이 달라짐. 먼저 `git status`, `git diff`, `git diff --staged`로 작업 폴더와 스테이지를 확인함. 아래 명령의 `README.md`는 실습용 파일임.

## add만 취소하고 수정은 남기기

첫 커밋이 만들어진 저장소에서 파일을 수정하고 `git add README.md`까지 한 상황임. 아직 커밋에는 넣고 싶지 않지만 파일의 수정은 유지하려면 다음처럼 실행함.

```powershell
git restore --staged README.md
```

스테이지의 해당 파일을 현재 커밋 `HEAD` 기준으로 되돌리고 작업 폴더의 수정은 그대로 둠. `git status`에서 스테이지에 있던 변경이 미등록 변경으로 바뀜. 첫 커밋 전에는 기본 복원 기준인 `HEAD`가 없으므로 이 명령을 그대로 사용할 수 없음.

## 파일의 미등록 수정 버리기

```powershell
git restore README.md
```

기본 동작은 스테이지에 기록된 내용으로 작업 파일을 복원함. 따라서 아직 `add`하지 않은 수정은 사라짐. 스테이지가 마지막 커밋과 같을 때는 결과적으로 파일이 마지막 커밋 상태로 돌아감. 추적 파일이 삭제된 상태에서도 스테이지에 기록이 있다면 이 방법으로 복원할 수 있음.

`add`한 뒤 더 수정했다면 위 명령은 추가 수정만 버리고 스테이지에 있는 내용은 남김. 스테이지와 작업 파일을 모두 마지막 커밋의 내용으로 되돌리려면 다음과 같음.

```powershell
git restore --source=HEAD --staged --worktree README.md
```

이 명령은 해당 파일의 staged와 unstaged 변경을 모두 덮어쓰므로 버릴 내용인지 확인한 뒤 사용함. 한 번도 추적하지 않은 파일은 Git에 이전 상태가 없어 같은 방식으로 복원할 수 없음. VS Code의 Discard Changes도 작업 내용을 실제로 버리는 동작이므로 Unstage와 구분함.

## 이미 만든 로컬 커밋의 위치 옮기기

`HEAD~1`은 현재 커밋의 첫 번째 부모. 커밋이 두 개 이상인 브랜치에서 `reset`을 실행하면 현재 브랜치가 가리키는 위치를 이전으로 옮길 수 있음. 어떤 내용을 남길지는 방식에 따라 다름.

| 명령 | 브랜치 위치 | 스테이지 | 작업 파일 |
| --- | --- | --- | --- |
| `git reset --soft HEAD~1` | 이전 커밋 | 유지 | 유지 |
| `git reset --mixed HEAD~1` | 이전 커밋 | 이전 커밋 상태 | 유지 |
| `git reset --hard HEAD~1` | 이전 커밋 | 이전 커밋 상태 | 이전 커밋 상태 |

`--mixed`가 기본값. soft는 되돌린 커밋의 내용이 스테이지에 남아 다시 커밋할 수 있고, mixed는 그 변경이 작업 폴더의 미등록 수정으로 남음. hard는 추적 파일의 미커밋 수정도 덮어쓰며 복원을 방해하는 미추적 파일도 삭제될 수 있음. 복구를 전제로 사용하지 말고 필요한 변경을 먼저 보관함.

## 공유한 이력을 남기며 변경 취소하기

```powershell
git revert --no-edit HEAD
```

`revert`는 지정한 커밋의 변경을 반대로 적용한 새 커밋을 만듦. 기존 커밋과 취소한 기록이 모두 이력에 남으므로 공유된 작업을 취소할 때 사용할 수 있음. 위 명령은 현재 일반 커밋을 대상으로 하고 특정 커밋은 해시로 지정함. 병합 커밋은 어느 부모를 기준으로 취소할지 추가 지정이 필요함.

진행 중 충돌하면 파일을 해결하고 `git add`한 뒤 `git revert --continue`로 이어감. 취소하려면 `git revert --abort`를 사용함. reset은 브랜치의 위치를 바꾸고 revert는 새로운 취소 커밋을 만든다는 차이를 기억함.

참고: [git restore](https://git-scm.com/docs/git-restore), [git reset](https://git-scm.com/docs/git-reset), [git revert](https://git-scm.com/docs/git-revert)

[이전](04-log-and-diff.md) | [다음](06-stash.md) | [목차로](../README.md)
