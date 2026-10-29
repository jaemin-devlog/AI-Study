# 자주 쓰는 명령어

## 확인하고 기록하기

| 할 일 | 명령어 |
| --- | --- |
| 현재 상태 | `git status` |
| 짧게 상태 보기 | `git status -sb` |
| 아직 add하지 않은 수정 | `git diff` |
| 다음 commit에 들어갈 내용 | `git diff --staged` |
| 파일을 stage에 올리기 | `git add topics/git-github/README.md` |
| commit하기 | `git commit -m "학습 메모 추가"` |
| 이력 보기 | `git log --oneline --graph --all --decorate` |

## 브랜치와 임시 보관

| 할 일 | 명령어 |
| --- | --- |
| 브랜치 목록 | `git branch` |
| 새 브랜치로 이동 | `git switch -c docs/git-note` |
| main으로 이동 | `git switch main` |
| 현재 브랜치에 작업 합치기 | `git merge docs/git-note` |
| 새 파일까지 잠깐 보관 | `git stash push -u -m "작성 중인 메모"` |
| stash 목록 | `git stash list` |
| 최근 stash 적용하고 목록 유지 | `git stash apply` |

## 원격과 주고받기

| 할 일 | 명령어 |
| --- | --- |
| 원격 주소 확인 | `git remote -v` |
| 원격 이력 가져오기 | `git fetch origin` |
| main에서 빠르게 최신 반영 | `git pull --ff-only origin main` |
| main 전송·업스트림 설정 | `git push -u origin main` |
| 연결된 브랜치로 push | `git push` |

pull 전 현재 브랜치와 미커밋 작업 확인

## 되돌리기

| 상황 | 명령어와 결과 |
| --- | --- |
| add만 취소 | `git restore --staged topics/git-github/README.md` · 파일 수정은 남음. 첫 commit 이후 사용. |
| add하지 않은 수정을 버림 | `git restore topics/git-github/README.md` · 작업 파일을 stage 내용으로 덮어씀. |
| 진행 중인 merge 취소 | `git merge --abort` |
| 진행 중인 rebase 취소 | `git rebase --abort` |

reset·revert 차이: [되돌리기](git/05-restore-reset-revert.md)

명령별 조건·공식 문서: [학습 노트](README.md)
