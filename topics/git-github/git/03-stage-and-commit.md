# add와 commit

## 작업 영역

| 위치 | 들어 있는 것 |
| --- | --- |
| 작업 폴더 | 직접 만들거나 수정하는 실제 파일 |
| 스테이지(index) | 다음 커밋에 넣을 파일 상태 |
| 로컬 저장소 | 커밋으로 남긴 이력 |

- `add`: 실행 시점의 파일 내용을 스테이지에 반영
- `commit`: 스테이지에 준비된 상태를 기록

## 커밋

```powershell
git status
git add topics/git-github/README.md
git diff --staged
git commit -m "Git 공부 기록 추가"
git status
```

- `git diff --staged`: 커밋에 들어갈 내용 확인

## status 읽기

| 표시 | 뜻 |
| --- | --- |
| `Untracked files` | 새로 생겼지만 아직 추적하지 않는 파일 |
| `Changes not staged for commit` | 추적 파일의 변경 중 아직 스테이지에 반영하지 않은 내용 |
| `Changes to be committed` | 다음 커밋에 들어갈 변경 |
| `nothing to commit, working tree clean` | 현재 Git이 보여주는 미커밋 변경 없음 |

- 새 파일: `add`로 추적 시작
- 기존 파일: 수정·삭제도 `add`로 반영

## add 후 추가 수정

- `topics/git-github/README.md`를 `add`한 뒤 수정한 부분: 스테이지에 미반영
- 같은 파일에 `Changes to be committed`와 `Changes not staged for commit` 동시 표시 가능

추가 수정 반영:

```powershell
git add topics/git-github/README.md
```

- `git add .`: 현재 폴더와 하위 폴더의 변경을 한꺼번에 반영
- 파일명 지정 시 커밋에 넣을 대상 선택 가능
- 커밋 메시지: 변경 내용 기록
- 관련 없는 변경은 커밋 분리. 이력 확인·되돌리기에 유리

참고: [git add](https://git-scm.com/docs/git-add), [git commit](https://git-scm.com/docs/git-commit), [git status](https://git-scm.com/docs/git-status)

[목차로](../README.md)
