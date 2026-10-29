# log와 diff

## 커밋 이력

```powershell
git log --oneline
git log --oneline --graph --all
git log --oneline -- topics/git-github/README.md
```

- `--oneline`: 커밋 하나를 한 줄로 표시
- `--graph --all`: 여러 브랜치의 이력을 연결해 표시
- `-- topics/git-github/README.md`: 해당 파일의 이력만 확인
- 앞의 짧은 영문·숫자: 커밋 해시의 일부
- `HEAD`: 현재 체크아웃한 커밋 참조. 브랜치 작업 중에는 보통 해당 브랜치를 통해 참조

현재 커밋의 메시지·변경 내용 확인:

```powershell
git show HEAD
```

## 커밋 전 비교

| 명령 | 비교하는 상태 |
| --- | --- |
| `git diff` | 스테이지와 작업 폴더. 아직 add하지 않은 변경 |
| `git diff --staged` | 현재 커밋과 스테이지. 다음 커밋에 넣을 변경 |
| `git diff HEAD` | 현재 커밋과 작업 폴더. 추적 파일의 전체 미커밋 변경 |

- Untracked 파일 내용: 기본 `git diff` 출력 대상에서 제외
- `add` 후 `git diff --staged`로 확인 가능

## 두 커밋 비교

전제: 커밋 두 개 이상.

```powershell
git diff HEAD~1 HEAD -- topics/git-github/README.md
```

- `HEAD~1`: 현재 커밋의 첫 번째 부모
- `HEAD~1`과 `HEAD` 비교: 부모 커밋과 현재 커밋 사이의 파일 변경
- 특정 시점 비교: 두 커밋 해시로 지정 가능
- diff 본문의 `-`: 이전 쪽에만 있는 줄
- diff 본문의 `+`: 이후 쪽에 추가된 줄
- 터미널 이력 화면 종료: `q`

참고: [git log](https://git-scm.com/docs/git-log), [git diff](https://git-scm.com/docs/git-diff), [git show](https://git-scm.com/docs/git-show)

[목차로](../README.md)
