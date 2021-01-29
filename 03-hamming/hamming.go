package hamming

import (
	"errors"
)

func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("")
	}

	hammingCount := 0

	for i := 0; i < len(a); i++ {
		if a[i] == b[i] {
			continue
		} else {
			hammingCount++
		}
	}
	return hammingCount, nil
}
