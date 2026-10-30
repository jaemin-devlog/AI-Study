# log와 diff

커밋을 기록했다면 이전에 어떤 작업을 했는지 확인하고 두 시점 사이에 무엇이 바뀌었는지 비교할 수 있음. `log`는 이력 목록, `diff`는 두 상태 사이의 내용 차이를 보여 줌.

## 커밋이 연결된 이력 읽기

```powershell
git log --oneline
git log --oneline --graph --all --decorate
git show HEAD
```

`--oneline`은 커밋을 짧은 해시와 메시지 한 줄로 표시함. `--graph`는 커밋의 연결을, `--all`은 여러 참조의 이력을 함께 보여 줌. `--decorate`는 브랜치나 태그가 가리키는 위치도 표시함. 화면이 긴 터미널 뷰어에서는 `q`로 빠져나갈 수 있음.

각 커밋은 보통 이전 커밋을 부모로 가리킴. `HEAD`는 현재 체크아웃한 위치를 나타내며 브랜치에 있을 때는 일반적으로 그 브랜치를 통해 현재 커밋을 가리킴. 특정 커밋을 직접 체크아웃한 detached HEAD 상태도 가능함. `git show HEAD`는 현재 커밋의 정보와 변경 내용을 확인함.

## 커밋하기 전 비교할 두 상태 정하기

| 명령 | 비교 대상 | 확인할 내용 |
| --- | --- | --- |
| `git diff` | 스테이지와 작업 폴더 | 아직 `add`하지 않은 추적 파일의 변경 |
| `git diff --staged` | 현재 커밋과 스테이지 | 다음 커밋에 들어갈 변경 |
| `git diff HEAD` | 현재 커밋과 작업 폴더 | 추적 파일의 스테이지와 미등록 변경을 합친 차이 |

`git add` 후 같은 파일을 다시 수정하면 두 영역이 모두 달라짐. 이때 `git diff`와 `git diff --staged`를 각각 보면 추가로 수정한 부분과 이미 준비된 부분을 구분할 수 있음. 아직 추적하지 않는 새 파일의 내용은 기본 `git diff`에 나오지 않으며 `git status`에서 확인하고 `add`한 뒤 스테이지 차이로 볼 수 있음.

## 두 커밋 사이 비교하기

```powershell
git log --oneline -- README.md
git diff HEAD~1 HEAD -- README.md
```

첫 명령은 해당 파일의 이력을 확인함. 둘째는 현재 커밋의 첫 번째 부모 `HEAD~1`과 현재 커밋 `HEAD` 사이에서 파일 내용이 어떻게 달라졌는지 보여 줌. 첫 커밋만 있다면 부모가 없으므로 이 비교는 사용할 수 없음. 두 해시를 직접 넣으면 더 떨어진 두 시점도 비교할 수 있음.

Diff 본문의 `-`는 앞의 상태에 있던 줄, `+`는 뒤의 상태에 추가된 줄임. `@@` 줄은 변경된 구간의 위치를 알려 주고 표시 없는 줄은 주변 문맥임. 색상뿐 아니라 어느 두 상태를 어느 순서로 비교했는지 먼저 확인해야 방향을 잘못 읽지 않음.

VS Code에서는 Source Control에서 현재 파일의 변경을 누르거나 파일의 Timeline에서 이전 기록을 선택해 비교할 수 있음. 다음에는 변경이 작업 폴더에만 있는지, 스테이지에 있는지, 이미 커밋됐는지에 따라 되돌리는 방법을 구분함.

참고: [git log](https://git-scm.com/docs/git-log), [git diff](https://git-scm.com/docs/git-diff), [git show](https://git-scm.com/docs/git-show)

[이전](03-stage-and-commit.md) | [다음](05-restore-reset-revert.md) | [목차로](../README.md)
